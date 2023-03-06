import pygame
from ExplorationMode.SubArea.Obstacle import Obstacle

class Wall(Obstacle):
    def __init__(self, x, y, width, height):
        if width == 800 and height == 30:
            super().__init__(x,y,'Images/Wall800x30.PNG')
        if width == 30 and height == 600:
            super().__init__(x,y,'Images/wall30x600.PNG')

    