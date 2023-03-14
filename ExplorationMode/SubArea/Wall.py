import pygame
from ExplorationMode.SubArea.Obstacle import Obstacle

class Wall(Obstacle):
    def __init__(self, x, y, width, height, imgPath):
        if width == 800 and height == 30:
            super().__init__(x,y,'Images\mapObjects\walls\800x30_wall.png')
        if width == 30 and height == 600:
            super().__init__(x,y,'Images\mapObjects\walls\\30x600_wall.png')

        #self.image = pygame.transform.scale(self.image, (width,height))
        #self.rect = self.image.get_rect()
        #self.rect.x = y
        #self.rect.y = x

    