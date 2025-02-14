import pygame

'''class Apple(pygame.sprite.Sprite):
    def __init__( self, x=0, y=0 ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/zombie.png')
        self.rect = self.image.get_rect()
        self.rect.center = ( x, y )'''


class Apple(pygame.sprite.Sprite):
    def __init__(self, vector, speed):
        super().__init__()
        self.image = pygame.image.load('UI\\apple0.1_0.png').convert_alpha()
        self.rect = self.image.get_rect()

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos

    def calcnewpos(self, rect, vector):
        x, y = vector
        dx = x * speed#speed * math.cos(angle)
        dy = y * speed#speed * math.sin(angle)
        return rect.move(dx, dy)

#https://www.pygame.org/docs/tut/tom_games4.html
#https://stackoverflow.com/questions/59889471/pygame-creating-a-enemy-class-and-then-importing-it-into-game