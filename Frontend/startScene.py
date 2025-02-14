import pygame
import sys


#def main():

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                import gameScene
                #gameScene.main()
                #running = False
                #return True



    screen.fill(WHITE)

    startBackground = pygame.image.load('E:\\Repository-DroneControl\\Images\\UI\\startBackground_0.png').convert_alpha()
    startBackground = pygame.transform.scale(startBackground, (width, height))
    screen.blit(startBackground, (0, 0))

    pygame.draw.rect(screen, RED, start_button, 0, 10)
    screen.blit(start_button_text, (int(width/2), int(height/2)))

    pygame.display.flip()
    
#pygame.quit()
#sys.exit()

#if __name__ == '__main__':
#    main()