import cv2
import mediapipe as mp
import pyautogui


def distance(pnt1, pnt2):
    return float(((pnt1[0] - pnt2[0])**2.0 + (pnt1[1] - pnt2[1])**2.0)**0.5)
def main():
    print('all libraries are imported!')


    camera = cv2.VideoCapture(0) # the variable "capture" is assigned to read the camera from port "0"
    screen_width, screen_height = pyautogui.size()
    pyautogui.FAILSAFE = False

    '''
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    '''

    mpHands = mp.solutions.hands
    mpDraw = mp.solutions.drawing_utils
    mpDrawStyles = mp.solutions.drawing_styles

    hands = mpHands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    
    points = [[float(0) for i in range(3)] for i in range(21)]
    for i in range(21):
        points[i][0] = float(0)
        points[i][1] = float(1)
        points[i][2] = int(-1)

    good, img = camera.read() # reading a frame from a camera to check access to the camera
    if good == False: 
        print('please check the camera, maybe another app is using the camera')

    while good:
        
        good, img = camera.read() # reading a frame from a camera
        img = cv2.flip(img, 1) # mirroring a frame vertically
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converting a frame from a camera
        
        camera_height = img.shape[0]
        camera_width = img.shape[1]


        results = hands.process(imgRGB)

        '''
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        '''
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(
                    img,  # image to draw
                    handLms,  # model output
                    mpHands.HAND_CONNECTIONS,  # hand connections
                    mpDrawStyles.get_default_hand_landmarks_style(),
                    mpDrawStyles.get_default_hand_connections_style())


        
            for id, point in enumerate(handLms.landmark):
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

            #print(results.multi_handedness[0].classification[0].label, results.multi_handedness[0].classification[0].label)
            #if distance(points[4], points[5]) < distance(points[6], points[8]):
            #    pyautogui.click()
            #print(f'{points[4][2]} {points[8][2]} {points[12][2]} {points[16][2]} {points[20][2]}')

            if points[8][2] == True and points[12][2] == True and points[16][2] == True and points[20][2] == True:
                        
                cursor_width = float((screen_width / camera_width) * width)
                cursor_height = float((screen_height / camera_height) * height)

                if cursor_width < 0: cursor_width = 0
                if cursor_width > screen_width: cursor_width = screen_width
                        
                if cursor_height < 0: cursor_height = 0
                if cursor_height > screen_height: cursor_height = screen_height
                pyautogui.moveTo(cursor_width, cursor_height)
                
            if distance(points[4], points[5]) < distance(points[6], points[8]):
                    pyautogui.click()
            #print(points[4][2], distance(points[4], points[5]), distance(points[5], points[13]))

            




                
        cv2.imshow('processed image from camera', img)
       
        if(cv2.waitKey(1) == ord('q')):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()












































































