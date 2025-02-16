import mediapipe as mp
import numpy as np
import pyautogui
import pickle
import cv2
import sys
import time

def main(isActive=False):
    print('All libraries are imported!')
    print('Please, waiting...')

    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']

    camera = cv2.VideoCapture(0)
    screen_width, screen_height = pyautogui.size()
    pyautogui.FAILSAFE = False

    position = (0, 0)
    #if not(isActive):
    #    isActive = False # The variable is changed in gameScene.py

    mpHands = mp.solutions.hands
    mpDraw = mp.solutions.drawing_utils
    mpDrawStyles = mp.solutions.drawing_styles

    hands = mpHands.Hands(static_image_mode=True, min_detection_confidence=0.3)
    labels_dict = {0: 'move', 1: 'click', 2: 'empty'}
    
    points = [[float(0) for i in range(3)] for i in range(21)]

    clickVer = 0
    good, img = camera.read() # reading a frame from a camera to check access to the camera
    if good == False: 
        print('Please, check the camera, maybe another app is using the camera')

    while True:
        while isActive and good:
            data_aux = []
            x_ = []
            y_ = []
            
            good, img = camera.read()   # reading a frame from a camera
            img = cv2.flip(img, 1)      # mirroring a frame vertically
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converting a frame from a camera
            
            camera_height = img.shape[0]
            camera_width = img.shape[1]

            results = hands.process(imgRGB)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for i in range(len(handLms.landmark)):
                        x = handLms.landmark[i].x
                        y = handLms.landmark[i].y

                        x_.append(x)
                        y_.append(y)

                    for i in range(len(handLms.landmark)):
                        x = handLms.landmark[i].x
                        y = handLms.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))


                x1 = int(min(x_) * camera_width) - 10
                y1 = int(min(y_) * camera_height) - 10

                x2 = int(max(x_) * camera_width) - 10
                y2 = int(max(y_) * camera_height) - 10


                try:
                    prediction = model.predict([np.asarray(data_aux)])

                    print(prediction[0])
                    if int(prediction[0]) == 0 or int(prediction[0]) == 1:
                        
                        width, height, color = img.shape
                        width, height = float(handLms.landmark[8].x * height), float(handLms.landmark[8].y * width)
                            
                        cursor_width = float((screen_width / camera_width) * width)
                        cursor_height = float((screen_height / camera_height) * height)

                        if cursor_width < 0: cursor_width = 0
                        if cursor_width > screen_width: cursor_width = screen_width
                                    
                        if cursor_height < 0: cursor_height = 0
                        if cursor_height > screen_height: cursor_height = screen_height
                        
                        pyautogui.moveTo(cursor_width, cursor_height)
                        position = (cursor_width, cursor_height)

                        if int(prediction[0]) == 1:
                            clickVer += 1
                            if clickVer >= 10:
                                pyautogui.click()
                                clickVer = 0
                            
                    if int(prediction[0]) != 1:
                        clickVer = 0
                        
                except Exception as e:
                    
                    if str(e) == 'X has 84 features, but RandomForestClassifier is expecting 42 features as input.':
                        print(f"Error: Keep your extra hand out of the camera's reach:\n{e}\n")
                    else:
                        print(f'Error: {e}\n')
def Exit():
    sys.exit()

    
#if __name__ == "__main__":
#    main(True)








































































