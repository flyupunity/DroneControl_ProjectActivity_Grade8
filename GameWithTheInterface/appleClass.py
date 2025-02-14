import pygame

class Apple(pygame.sprite.Sprite):
    def __init__( self, x=0, y=0 ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/zombie.png')
        self.rect = self.image.get_rect()
        self.rect.center = ( x, y )



#https://stackoverflow.com/questions/59889471/pygame-creating-a-enemy-class-and-then-importing-it-into-game