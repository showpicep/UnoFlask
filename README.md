# UnoFlask
## Important!
First, you need to download the model itself in onnx extension. This can be done by clicking on the following link: [Uno_detector.onnx](https://drive.google.com/file/d/1QISl22qaUhZm7DxIJuM2ctDrV9t2UBSO/view?usp=sharing).
Then move the downloaded file to the "model" folder.
___
## Running
1. Download and run Docker.
2. Execute the following commands:
- Build Docker image using: docker build -t web-detector . 
- Run Docker container using: --rm --name detector -p 5000:5000 web-detector
___
## Source code
- [model/Detect.py](https://github.com/showpicep/UnoFlask/blob/main/model/Detect.py) contains functions for processing the results obtained from the model.
- [tamplates](https://github.com/showpicep/UnoFlask/tree/main/templates) contains the code responsible for the appearance of the home page.
- [Dockerfile](https://github.com/showpicep/UnoFlask/blob/main/Dockerfile) contains instructions for starting the application.
- [Uno.ipynb](https://github.com/showpicep/UnoFlask/blob/main/Uno.ipynb) contains code describing the learning process of the neural network.
- [main.py](https://github.com/showpicep/UnoFlask/blob/main/main.py) contains the logic of the site.
___
## Example of interaction with the site.
1. After starting Docker, go to http://localhost:5000.
![Image1](https://github.com/showpicep/UnoFlask/blob/main/static/MainPage.jpg)
2. Select the file and press the "Detect" button.
![Image2](https://github.com/showpicep/UnoFlask/blob/main/static/Result.jpg)
