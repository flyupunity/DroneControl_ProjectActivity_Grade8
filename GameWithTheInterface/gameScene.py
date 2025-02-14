import pygame
import sys

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

font = pygame.font.SysFont(None, 55)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button.collidepoint(event.pos):
                #running = False
                import startScene


    screen.fill(WHITE)

    # Background
    gameBackground = pygame.image.load('UI\\Background1.1_0.png').convert_alpha()
    gameBackground = pygame.transform.scale(gameBackground, (width, height))
    screen.blit(gameBackground, (0, 0))


    # Table
    table = pygame.image.load('UI\\table0_0.png').convert_alpha()
    table = pygame.transform.scale(table, (width*0.5, height*0.5))
    screen.blit(table, (width*0, height*0.8))
    

    # Apple
    apple = pygame.image.load('UI\\apple0_0.png').convert_alpha()
    apple = pygame.transform.scale(apple, (apple.get_width()/6, apple.get_height()/6))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(apple, (mouse_x - int(apple.get_height()/2), mouse_y - int(apple.get_width()/2)))


    # Basket
    basket = pygame.image.load('UI\\basket0_0.png').convert_alpha()
    basket = pygame.transform.scale(basket, (basket.get_width()*0.3, basket.get_height()*0.3))
    screen.blit(basket, (width*1-basket.get_width()*2, height*0.6))



    # Exit button
    exit_button = pygame.Rect(50, 25, 400, 50)
    pygame.draw.rect(screen, RED, exit_button, 0, 10)

    # Exit text
    exit_text = font.render("Back to main menu", True, WHITE)
    exit_text_rect = exit_text.get_rect()
    
    exit_text_rect.center = (exit_button.x + exit_button.w // 2, exit_button.y + exit_button.h // 2)
    screen.blit(exit_text, exit_text_rect.topleft)





    #Display update
    pygame.display.update()
    #pygame.display.flip()
    
#pygame.quit()
#sys.exit()