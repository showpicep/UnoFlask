import cv2
import numpy as np
import onnxruntime as onnxrt


CLASSES = [
    '__background__', '11', '9', '13', '10', '6', '7', '0', '5', '4', '2', '14',
    '8', '12', '1', '3'
]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
DETECTION_THRESHOLD = 0.8


def GetPreds(image):
    """
    Функция, возвращающая словарь (для удобного взаимодействия с полученными от модели результатами)
    :param image: На вход подается изображение, значения которого находятся в диапозоне [0, 1]
    (np.array) с размерностью (1, 3, 416, 416)
    :return: Возвращет словарь, содержищий в себе:
    ['boxes'] ключевые точки для отрисовки границ объекта,
    ['labels'] предсказанные классы
    ['scores'] и их вероятность
    """
    onnx_session = onnxrt.InferenceSession("model/Uno_detector.onnx")
    onnx_inputs = {onnx_session.get_inputs()[0].name: image}
    onnx_output = onnx_session.run(None, input_feed=onnx_inputs)
    res = {}
    keys = ['boxes', 'labels', 'scores']
    for idx, key in enumerate(keys):
        res[key] = onnx_output[idx]
    return res


def SaveDetectedImage(path: str):
    """
    Функция, предназначенная для записи изображения с размеченными границами объектов и их предсказанными классами
    :param path: Путь до изображения, которое будет подаваться в модель
    :return: Записываем конечное изображение в static/Detected.jpg
    """
    image = cv2.imread(path)
    orig_image = image.copy()
    # BGR to RGB
    image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB).astype(np.float32)
    # make the pixel range between 0 and 1
    image = cv2.resize(image, (416, 416))
    image /= 255.0
    # bring color channels to front
    image = np.transpose(image, (2, 0, 1)).astype(np.float32)
    # add batch dimension

    image = np.expand_dims(image, 0)
    print(image.shape)
    # image.shape = (1, 3, 416, 416)

    res = GetPreds(image)
    if len(res['boxes']) != 0:
        boxes = res['boxes']
        scores = res['scores']
        # filter out boxes according to `detection_threshold`
        boxes = boxes[scores >= DETECTION_THRESHOLD].astype(np.int32)
        draw_boxes = boxes.copy()
        # get all the predicited class names
        pred_classes = [CLASSES[i] for i in res['labels']]

        # draw the bounding boxes and write the class name on top of it
        for j, box in enumerate(draw_boxes):
            class_name = pred_classes[j]
            color = COLORS[CLASSES.index(class_name)]
            cv2.rectangle(orig_image,
                          (int(box[0]), int(box[1])),
                          (int(box[2]), int(box[3])),
                          color, 2)
            cv2.putText(orig_image, class_name,
                        (int(box[0]), int(box[1] - 5)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color,
                        2, lineType=cv2.LINE_AA)
        cv2.imwrite("static/Detected.jpg", orig_image)
