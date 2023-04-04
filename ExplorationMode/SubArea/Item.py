import pygame
from GameObject import GameObject

class Item(GameObject):
    def __init__(self, moneyValue, crystalValue,xpValue, x, y, room, imgPath):
        super().__init__(x, y, imgPath)
        self.moneyValue = moneyValue
        self.crystalValue = crystalValue
        self.xpValue = xpValue
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.room = room