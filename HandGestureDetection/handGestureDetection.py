import cv2
import mediapipe as mp
import wmi
import pyautogui

print("0) Mouse Cursor Control")
print("1) Brightness and sound control")
print("2) Brightness 2.0")
print("3) Mouse Cursor Click")

mode = int(input())
good, img = camera.read()

if good == False:
    print("please check the camera, maybe another app is using the camera")

while good:
    
    good, img = camera.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    camera_height = img.shape[0]
    camera_width = img.shape[1]


    cv2.imshow("image", img)
   
    if(cv2.waitKey(1) == ord('q')):
        break

camera.release()
cv2.destroyAllWindows()








































