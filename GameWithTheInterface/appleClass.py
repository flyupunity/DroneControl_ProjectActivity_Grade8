import pygame

'''class Apple(pygame.sprite.Sprite):
    def __init__( self, x=0, y=0 ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/zombie.png')
        self.rect = self.image.get_rect()
        self.rect.center = ( x, y )'''


class Apple(object):
    def __init__(self, startPos_x, startPos_y):
        super().__init__()

        self.x = startPos_x
        self.y = startPos_y

        self.image = pygame.image.load('UI\\apple0.1_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/2, self.image.get_height()/2))

        self.image_rect = self.image.get_rect()

        self.isDragged = False

        #screen = pygame.display.get_surface()
        #self.area = screen.get_rect()

    def draw(self, screen):

        self.image_rect = self.image.get_rect()
        print(self.image.get_rect())

        if self.isDragged:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if self.deviation_x == 0 or self.deviation_y == 0:
                self.deviation_x = mouse_x - self.x
                self.deviation_y = mouse_y - self.y
            
            self.x, self.y = mouse_x - self.deviation_x, mouse_y - self.deviation_y
            
        else:
            self.deviation_x = 0
            self.deviation_y = 0

        self.image.get_rect().x = self.x
        self.image.get_rect().y = self.x
        screen.blit(self.image, (self.x, self.y))

    def CheckingTheDragging(self, isDragged):
        self.isDragged = isDragged
        print(isDragged)


        



#https://www.pygame.org/docs/tut/tom_games4.html
#https://stackoverflow.com/questions/59889471/pygame-creating-a-enemy-class-and-then-importing-it-into-game
#https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/optimization



