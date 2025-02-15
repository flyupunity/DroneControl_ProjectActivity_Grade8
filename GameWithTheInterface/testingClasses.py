import pygame
import sys
import appleClass

pygame.init()

width, height = pygame.display.set_mode().get_size()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

font = pygame.font.SysFont(None, 55)

appleFromClass = appleClass.Apple(0, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            elif appleFromClass.image_rect.collidepoint(event.pos):
                appleFromClass.CheckingTheDragging(True)
        elif event.type == pygame.MOUSEBUTTONUP:
            appleFromClass.CheckingTheDragging(False)

    screen.fill((255, 255, 255))
    appleFromClass.draw(screen)




    # Exit button
    exit_button = pygame.Rect(50, 25, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), exit_button, 0, 10)

    # Exit text
    exit_text = font.render("Exit", True, (255, 255, 255))
    exit_text_rect = exit_text.get_rect()
    
    exit_text_rect.center = (exit_button.x + exit_button.w // 2, exit_button.y + exit_button.h // 2)
    screen.blit(exit_text, exit_text_rect.topleft)


    #Display update
    pygame.display.update()
    




'''import pygame
import math
import os
import sys

def load_png(name):
    """Load image and return image object with rect"""
    fullname = os.path.join('', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as e:
        print(f'Cannot load image: {fullname}')
        raise SystemExit(e)
    return image, image.get_rect()

class Ball(pygame.sprite.Sprite):
    """A ball that moves across the screen"""
    def __init__(self, vector):
        super().__init__()
        self.image, 
        self.rect = load_png('UI\\apple0.1_0.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector  # (angle in radians, speed)

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos

    def calcnewpos(self, rect, vector):
        angle, speed = vector
        dx = speed * math.cos(angle)
        dy = speed * math.sin(angle)
        return rect.move(dx, dy)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Ball Movement')
    clock = pygame.time.Clock()

    # Initialize ball with 45 degree angle and 5px/frame speed
    ball = Ball((math.radians(45), 3))
    all_sprites = pygame.sprite.Group(ball)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        all_sprites.draw(screen)  # Draw sprites
        pygame.display.flip()  # Update display


    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
'''





'''import pygame

class Ball:
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('UI\\apple0.1_0.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

def main():
    ball = Ball()

    while True:
        ball.update()
    
if __name__ == '__main__':
    main()'''