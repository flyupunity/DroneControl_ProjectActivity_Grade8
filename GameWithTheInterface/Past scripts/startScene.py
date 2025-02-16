import pygame
import sys
import importlib


#def main():

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
                    import gameScene
                #gameScene.main()
                #running = False
                #return True





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
    
#pygame.quit()
#sys.exit()

#if __name__ == '__main__':
#    main()