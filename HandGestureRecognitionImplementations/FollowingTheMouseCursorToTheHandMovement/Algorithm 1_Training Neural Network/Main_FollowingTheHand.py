import mediapipe as mp
import numpy as np
import pyautogui
import pickle
import cv2

def main():
    print('All libraries are imported!')
    print('Please, waiting...')

    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']

    camera = cv2.VideoCapture(0) # the variable "capture" is assigned to read the camera from port "0"
    screen_width, screen_height = pyautogui.size()
    pyautogui.FAILSAFE = False


    mpHands = mp.solutions.hands
    mpDraw = mp.solutions.drawing_utils
    mpDrawStyles = mp.solutions.drawing_styles

    hands = mpHands.Hands(static_image_mode=True, min_detection_confidence=0.3)
    labels_dict = {0: 'move', 1: 'click', 2: 'empty'}
    
    points = [[float(0) for i in range(3)] for i in range(21)]
    '''
    for i in range(21):
        points[i][0] = float(0)
        points[i][1] = float(1)
        points[i][2] = int(-1)
    '''
    clickVer = 0
    good, img = camera.read() # reading a frame from a camera to check access to the camera
    if good == False: 
        print('Please, check the camera, maybe another app is using the camera')

    while good:

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
                mpDraw.draw_landmarks(
                    img,                        # image to draw
                    handLms,                    # model output
                    mpHands.HAND_CONNECTIONS,   # hand connections
                    mpDrawStyles.get_default_hand_landmarks_style(),
                    mpDrawStyles.get_default_hand_connections_style())



            '''for id, point in enumerate(handLms.landmark):
                width, height, color = img.shape
                width, height = float(point.x * height), float(point.y * width)

                points[id][0] = width
                points[id][1] = height

                if id == 8 or id == 12 or id == 16 or id == 20: # check for finger raised points
                    #Is your finger raised with the ID number?
                    if distance(points[0], points[id]) <= distance(points[0], points[id - 3]):
                        points[id][2] = 0 # no, the finger is not raised
                    
                    elif distance(points[0], points[id]) > distance(points[0], points[id - 3]): 
                        points[id][2] = 1 # yes, thumbs up
            
            if distance(points[4], points[5]) > distance(points[5], points[13]):
                points[4][2] = 1
            else:
                points[4][2] = 0
            '''
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
                predicted_character = labels_dict[int(prediction[0])]

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                cv2.putText(img, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                            cv2.LINE_AA)

                
                if int(prediction[0]) == 0:
                    
                    width, height, color = img.shape
                    width, height = float(handLms.landmark[8].x * height), float(handLms.landmark[8].y * width)
                     
                    cursor_width = float((screen_width / camera_width) * width)
                    cursor_height = float((screen_height / camera_height) * height)

                    if cursor_width < 0: cursor_width = 0
                    if cursor_width > screen_width: cursor_width = screen_width
                                
                    if cursor_height < 0: cursor_height = 0
                    if cursor_height > screen_height: cursor_height = screen_height
                    
                    pyautogui.moveTo(cursor_width, cursor_height)
                    
                elif int(prediction[0]) == 1:
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
           
                
        cv2.imshow('processed image from camera', img)
       
        if(cv2.waitKey(1) == ord('q')):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    

#pyautogui.click()
#pyautogui.mouseUp()
#pyautogui.mouseDown()
#pyautogui.drag(0, -distance, duration=0.5, button='left')
    
#print(results.multi_handedness[0].classification[0].label, results.multi_handedness[0].classification[0].label)
#if distance(points[4], points[5]) < distance(points[6], points[8]):
#print(f'{points[4][2]} {points[8][2]} {points[12][2]} {points[16][2]} {points[20][2]}')









































































