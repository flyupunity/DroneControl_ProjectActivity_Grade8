# About the project

This is my project "Drone Control" for "Project Activity" for the 8th grade created in Python. The task of which is to control the drone by reading hand gestures using a camera. The project is divided into several parts. At the moment, recognition of 5 basic gestures has been implemented in the form of a temporary solution - control of the course mouse of the computer
<br>

> [!TIP]
> - To edit scripts, you can use the [web version of Visual Studio Code](https://vscode.dev/)
> - To run scripts you can use [Colab Colaboratory](https://colab.research.google.com/)

> [!IMPORTANT]
> #### Requirements
>
>
> -  The application requires a ***camera***
> - [`Python`](https://www.python.org/downloads/) (I use version "3.10" and "3.12" for work)
> - [Libraries for Python (`mediapipe`, `pyautogui`, `opencv`)](#installation-on-windows-using-cmd)

<br><br>




# Getting started

>[!WARNING]
>### Рroject in development
> At the moment, the first part of the project has been implemented, which recognizes hand gestures and moves the computer mouse cursor, consisting of code.

>[!IMPORTANT]
>### To ensure that hand gestures are recognized correctly<br>
  > 1. The camera should only see one hand<br>
  > 2. Keep your hand parallel to the camera, palm facing the camera<br>
>
> ***otherwise hand recognition will be incorrect!***
>

<br>

## Installation on Windows using cmd
  Download and place anywhere on your computer

  #### Virtual environment
  ```cmd
  cd "[path to the project]\HandGestureDetection\"
  py -m venv venv
  .\venv\Scripts\activate
  ```

  #### Updating the pip package of the virtual environment
  ```cmd
  python.exe -m pip install --upgrade pip
  ```
  
  #### Write project dependencies in "requirements.txt"
  ```cmd
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```
  #### Installing libraries for Python
  ```cmd
  pip install mediapipe
  pip install pyautogui
  pip install opencv-python
  ```
<br>

## Launch the first part of the project
To run the project, enter the following commands in CMD:
```
cd "[path to the project]\HandGestureDetection\"
.\venv\Scripts\activate
main_handGestureDetection.py
```
> [!NOTE]
> Wait about 30 seconds for the script to run.
> After importing the script libraries, a window will open showing the processed image from the camera. Show ***one*** hand to the camera and be surprised that all 21 landmarks are displayed.
> After that, try making hand gestures from the table below to understand what each gesture does

<p align="center"><img src=".\images\hand_landmarks_002.png" height="200em"/></p>

### Hand gestures
> [!IMPORTANT]
> ***Here I would like to remind you that the project is currently being developed and the meaning of gestures will soon change.***

| Number |                Hand gesture image                      | Action these hand gestures |
|-------:|--------------------------------------------------------|----------------------------|
|       1| <p align="center"><img src=".\Images\handGesture_1st_up.jpg" height="50em"/></p>| computer mouse cursor moves `up`|
|       2| <p align="center"><img src=".\Images\handGesture_2nd_right.jpg" height="50em"/></p>|  computer mouse cursor moves to the `right`|
|       3| <p align="center"><img src=".\Images\handGesture_3rd_left.jpg" height="50em"/></p>|  computer mouse cursor moves to the `left`
|       4| <p align="center"><img src=".\Images\handGesture_4th_down.jpg" height="50em"/></p>|  computer mouse cursor moves `down`|
|       5| <p align="center"><img src=".\Images\handGesture_5th_specialAction.jpg" height="50em"/></p>|  this is a special action and at the moment if you make this gesture then the computer mouse will `press the left button`|

## ***Stopping*** the script

> [!NOTE]
> To stop the program, you can either 1. close the console, or 2. make sure that the window with the camera image is in active mode (it can be activated by clicking the left mouse button), and after making sure that you have selected the English keyboard layout, press the Q button


