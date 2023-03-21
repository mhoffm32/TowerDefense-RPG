
from GameObject import GameObject
import pygame

class Troop(GameObject):
    def __init__(self,x,y,width, height, img_path):
        #initialize other troop specific attributes
        super().__init__(x,y,img_path)
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y