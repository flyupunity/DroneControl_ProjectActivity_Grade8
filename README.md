## Drone control for project activities in 8th grade

Drone control for "Project activity" for grade 8. By reading hand gestures and recognizing the head/body
<br>

> [!IMPORTANT]
> #### Requirements
>
>
> -  The application requires a ***camera***
> - [`Python`](https://www.python.org/downloads/) (I use version "3.10" and "3.12" for work)
> - [Libraries for Python (`mediapipe`, `pyautogui`, `opencv`)](#installation-on-windows-using-cmd)

<br><br>




  
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
  
  #### Creating a file with a list of installed libraries in the file "requirements.txt"
  ```cmd
  pip install requests
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```
  #### Installing libraries for Python
  ```cmd
  pip install mediapipe
  pip install pyautogui
  pip install opencv-python
  ```
