import pygame
import sys
import appleClass
import random


def main():
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


    #appleFromClass = appleClass.Apple(((1, 1), 1, 1))
    #all_sprites = pygame.sprite.Group(appleFromClass)
    applesFromClass = [appleClass.Apple(random.randrange(1341, 1446), random.randrange(701, 729)) for _ in range(5)]


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

if __name__ == '__main__':
    main()
    
