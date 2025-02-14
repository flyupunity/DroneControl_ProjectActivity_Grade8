import pygame
import sys

pygame.init()

#window_size = (800, 600)
width, height = pygame.display.set_mode().get_size()
window_size = (width, height)

screen = pygame.display.set_mode(window_size)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("User Interface")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont(None, 55)

start_button = pygame.Rect(int(width/2), int(height/2), 200, 50)
start_button_text = font.render("Start", True, BLACK)

exit_button = pygame.Rect(50, 25, 100, 50)
exit_button_text = font.render("Exit", True, BLACK)

game_started = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game_started = True
            if exit_button.collidepoint(event.pos) and game_started:
                running = False


    screen.fill(WHITE)

    if not game_started:
        startBackground = pygame.image.load('E:\\Repository-DroneControl\\Images\\UI\\startBackground_0.png').convert_alpha()
        startBackground = pygame.transform.scale(startBackground, (width, height))
        screen.blit(startBackground, (0, 0))

        pygame.draw.rect(screen, RED, start_button, 0, 10)
        screen.blit(start_button_text, (int(width/2), int(height/2)))

    else:
        gameBackground = pygame.image.load('E:\\Repository-DroneControl\\Images\\UI\\Background1.1_0.png').convert_alpha()
        gameBackground = pygame.transform.scale(gameBackground, (width, height))
        screen.blit(gameBackground, (0, 0))

        table = pygame.image.load('E:\\Repository-DroneControl\\Images\\UI\\table0_0.png').convert_alpha()
        table = pygame.transform.scale(table, (width*0.5, height*0.5))
        screen.blit(table, (width*0, height*0.8))
        
        apple = pygame.image.load('E:\\Repository-DroneControl\\Images\\UI\\apple0_0.png').convert_alpha()
        apple = pygame.transform.scale(apple, (apple.get_width()/6, apple.get_height()/6))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(apple, (mouse_x - int(apple.get_height()/2), mouse_y - int(apple.get_width()/2)))

        basket = pygame.image.load('E:\\Repository-DroneControl\\Images\\UI\\basket0_0.png').convert_alpha()
        basket = pygame.transform.scale(basket, (basket.get_width()*0.3, basket.get_height()*0.3))
        screen.blit(basket, (width*1-basket.get_width()*2, height*0.6))

        pygame.draw.rect(screen, RED, exit_button, )
        screen.blit(exit_button_text, (50, 25))

    #pygame.display.update()
    pygame.display.flip()
    
pygame.quit()
sys.exit()