import pygame
from ExplorationMode.SubArea.Obstacle import Obstacle

class Wall(Obstacle):
    def __init__(self, x, y, width, height, imgPath):
        #if width == 1000 and height == 38:
        #    super().__init__(x,y,'Images/mapObjects/walls/1000x38_wall.png')
        #if width == 35 and height == 700:
        #    super().__init__(x,y,'Images/mapObjects/walls/35x700_wall.png')


        super().__init__(x,y,imgPath)

        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    