from flask import Flask, render_template, send_from_directory, request
import os
from model.Detect import SaveDetectedImage

app = Flask(__name__)


@app.route("/")
def style():
    """
    Функция, отвечающая за содержимое начальной страницы сайта
    :return:
    """
    return render_template("MainPage.html", image_loc='back.jpg')


@app.route('/', methods=['POST'])
def handle_data():
    """
    Функция, отвечающая за обработку загруженного изображения.
    :return:
    """
    image_file = request.files['image']
    image_location = os.path.join(
        'static/',
        'detect.jpg'
        # image_file.filename
    )
    if image_file:
        image_file.save(image_location)
        SaveDetectedImage(image_location)
    else:
        return render_template("MainPage.html", image_loc='back.jpg')

    return render_template("MainPage.html", image_loc='Detected.jpg')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
