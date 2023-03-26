
from GameObject import GameObject
import pygame

class Troop(GameObject):
    def __init__(self,x,y,width, height, img_path):
        #initialize other troop specific attributes
        super().__init__(x,y,img_path)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def setPosition(self, slotNumber):
        if slotNumber == 0:
            self.rect.x = 421
            self.rect.y = 271
        elif slotNumber == 1:
            self.rect.x = 579
            self.rect.y = 429
        elif slotNumber == 2:
            self.rect.x = 579
            self.rect.y = 271
        elif slotNumber == 3:
            self.rect.x = 421
            self.rect.y = 429
        elif slotNumber == 4:
            self.rect.x = 452
            self.rect.y = 271
        elif slotNumber == 5:
            self.rect.x = 548
            self.rect.y = 429
        elif slotNumber == 6:
            self.rect.x = 421
            self.rect.y = 398
        elif slotNumber == 7:
            self.rect.x = 548
            self.rect.y = 271
        elif slotNumber == 8:
            self.rect.x = 421
            self.rect.y = 302
        elif slotNumber == 9:
            self.rect.x = 579
            self.rect.y = 398
        elif slotNumber == 10:
            self.rect.x = 452
            self.rect.y = 429
        elif slotNumber == 11:
            self.rect.x = 579
            self.rect.y = 302
        elif slotNumber == 12:
            self.rect.x = 421
            self.rect.y = 333
        elif slotNumber == 13:
            self.rect.x = 579
            self.rect.y = 367
        elif slotNumber == 14:
            self.rect.x = 483
            self.rect.y = 429
        elif slotNumber == 15:
            self.rect.x = 517
            self.rect.y = 271
        elif slotNumber == 16:
            self.rect.x = 483
            self.rect.y = 271
        elif slotNumber == 17:
            self.rect.x = 517
            self.rect.y = 429
        elif slotNumber == 18:
            self.rect.x = 579
            self.rect.y = 333
        elif slotNumber == 19:
            self.rect.x = 421
            self.rect.y = 367