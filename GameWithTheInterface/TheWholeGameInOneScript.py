import mediapipe as mp
import numpy as np
import pyautogui
import pickle
import cv2
import pygame
import sys
#import appleClass
#import followingTheHand
import random

class Apple(object):
    def __init__(self, startPos_x, startPos_y):
        #super().__init__()

        self.x = startPos_x
        self.y = startPos_y

        self.image = pygame.image.load('UI\\apple0.1_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//2, self.image.get_height()//2))

        self.image_rect = self.image.get_rect(topleft=(self.x, self.y))
        self.isDragged = False

        self.deviation_x = 0
        self.deviation_y = 0

        #screen = pygame.display.get_surface()
        #self.area = screen.get_rect()

    def draw(self, screen):

        if self.isDragged:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            self.x = mouse_x - self.deviation_x
            self.y = mouse_y - self.deviation_y


        self.image_rect.topleft = (self.x, self.y)
        screen.blit(self.image, (self.x, self.y))

    def CheckingTheDragging(self, isDragged):
        self.isDragged = isDragged
        if isDragged:
            x, y = pygame.mouse.get_pos()
            self.deviation_x = x - self.x
            self.deviation_y = y - self.y
        else:
            self.deviation_x = 0
            self.deviation_y = 0

def main():
    print('All libraries are imported!')
    print('Please, waiting...')
    pygame.init()


    #window_size = (800, 600)
    width, height = pygame.display.set_mode().get_size()
    window_size = (width, height)

    #screen = pygame.display.set_mode(window_size)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption("User Interface")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)




    font = pygame.font.SysFont(None, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif start_button.collidepoint(event.pos):
                    running = False





        screen.fill(WHITE)

        #Background
        startBackground = pygame.image.load('UI\\startBackground_0.png').convert_alpha()
        startBackground = pygame.transform.scale(startBackground, (width, height))
        screen.blit(startBackground, (0, 0))



        #Start button
        #start_button = pygame.Rect(width//2, height//2 - (50)/2, 200, 50)
        start_button = pygame.Rect(0, 0, 400, 100)
        start_button.center = (width // 2, height // 2 - (100)/1.5 + 200)
        pygame.draw.rect(screen, RED, start_button, 0, 20)
        
        #Start text
        start_text = font.render("Start", True, WHITE)

        start_text_rect = start_text.get_rect()
        start_text_rect.center = (start_button.x + start_button.w // 2, start_button.y + start_button.h // 2)
        screen.blit(start_text, start_text_rect.topleft)




        #Exit button
        exit_button = pygame.Rect(0, 0, 400, 100)
        exit_button.center = (width // 2, height // 2 + (100)/1.5 + 200)
        pygame.draw.rect(screen, RED, exit_button, 0, 20)

        #Exit text
        exit_text = font.render("Exit", True, WHITE)

        exit_text_rect = exit_text.get_rect()
        exit_text_rect.center = (exit_button.x + exit_button.w // 2, exit_button.y + exit_button.h // 2)
        screen.blit(exit_text, exit_text_rect.topleft)



        #Name text - https://www.pygame.org/pcr/hollow_outline/index.php

        font = pygame.font.SysFont(None, 100)
        NAME_TEXT = (0, 0, 0)


        name_text = font.render(f"CONTROL OF THE MOUSE COURSE", True, NAME_TEXT)
        name_text_rect = name_text.get_rect()
        name_text_rect.center = (width // 2, 150)
        screen.blit(name_text, name_text_rect.topleft)

        name_text = font.render(f"BY HAND GESTURES", True, NAME_TEXT)
        name_text_rect = name_text.get_rect()
        name_text_rect.center = (width // 2, 250)
        screen.blit(name_text, name_text_rect.topleft)

        name_text = font.render(f"USING NEURAL NETWORKS", True, NAME_TEXT)
        name_text_rect = name_text.get_rect()
        name_text_rect.center = (width // 2, 350)
        screen.blit(name_text, name_text_rect.topleft)

        name_text = font.render(f"VIA USER INTERFACE", True, NAME_TEXT)
        name_text_rect = name_text.get_rect()
        name_text_rect.center = (width // 2, 450)
        screen.blit(name_text, name_text_rect.topleft)
        
        #screen.blit(name_text, (width // 2, 300))

        #name_text_rect = name_text.get_rect()
        #name_text_rect.center = (0, name_button.y + name_button.h // 2)
        #screen.blit(name_text, (width // 2, ))




        #Display update
        pygame.display.update()
        #pygame.display.flip()











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












    font = pygame.font.SysFont(None, 55)
    applesFromClass = [Apple(random.randrange(1341, 1446), random.randrange(701, 729)) for _ in range(5)]


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    #running = False
                    #import startScene
                    pygame.quit()
                    sys.exit()
                elif event.button == 1:
                    for apple in applesFromClass:
                        if apple.image_rect.collidepoint(event.pos):
                            apple.CheckingTheDragging(True)
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for apple in applesFromClass:
                        apple.CheckingTheDragging(False)

        screen.fill(WHITE)

        

        # Background
        gameBackground = pygame.image.load('UI\\Background1.2_0.png').convert_alpha()
        gameBackground = pygame.transform.scale(gameBackground, (width, height))
        screen.blit(gameBackground, (0, 0))


        # Table
        table = pygame.image.load('UI\\table0_0.png').convert_alpha()
        table = pygame.transform.scale(table, (width*0.5, height*0.5))
        screen.blit(table, (width*0, height*0.8))
        

        # Apple
        for apple in applesFromClass:
            apple.draw(screen)
        #all_sprites.update()
        #all_sprites.draw(screen)


        # Basket
        basket = pygame.image.load('UI\\basket0_0.png').convert_alpha()
        basket = pygame.transform.scale(basket, (basket.get_width()*0.3, basket.get_height()*0.3))
        screen.blit(basket, (width*1-basket.get_width()*2, height*0.6))



        # Exit button
        #exit_button = pygame.Rect(50, 25, 400, 50)
        exit_button = pygame.Rect(50, 25, 200, 50)
        pygame.draw.rect(screen, RED, exit_button, 0, 10)

        # Exit text
        #exit_text = font.render("Back to main menu", True, WHITE)
        exit_text = font.render("Exit", True, WHITE)
        exit_text_rect = exit_text.get_rect()
        
        exit_text_rect.center = (exit_button.x + exit_button.w // 2, exit_button.y + exit_button.h // 2)
        screen.blit(exit_text, exit_text_rect.topleft)



        #Display update
        pygame.display.update()
        #pygame.display.flip()






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
                    
                    width_hand, height_hand, color = img.shape
                    width_hand, height_hand = float(handLms.landmark[8].x * height), float(handLms.landmark[8].y * width_hand)
                        
                    cursor_width = float((screen_width / camera_width) * width_hand)
                    cursor_height = float((screen_height / camera_height) * height_hand)

                    if cursor_width < 0: cursor_width = 0
                    if cursor_width > screen_width: cursor_width = screen_width
                                
                    if cursor_height < 0: cursor_height = 0
                    if cursor_height > screen_height: cursor_height = screen_height
                    

                    position = (cursor_width, cursor_height)

                    if int(prediction[0]) == 0:
                        pyautogui.moveTo(cursor_width, cursor_height)
                    if int(prediction[0]) == 1:
                        pyautogui.mouseDown()
                        pyautogui.moveTo(cursor_width, cursor_height)
                        
                        
                        #pyautogui.dragTo(cursor_width, cursor_height, button='left')
                        #clickVer += 1
                        #if clickVer >= 10:
                        #    pyautogui.click()
                        #    clickVer = 0
                        
                if int(prediction[0]) != 1:
                    clickVer = 0
                    
            except Exception as e:
                
                if str(e) == 'X has 84 features, but RandomForestClassifier is expecting 42 features as input.':
                    print(f"Error: Keep your extra hand out of the camera's reach:\n{e}\n")
                else:
                    print(f'Error: {e}\n')

if __name__ == '__main__':
    main()
    
