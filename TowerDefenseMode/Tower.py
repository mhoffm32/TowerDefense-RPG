from GameObject import GameObject
import pygame

class Tower(GameObject):
    def __init__(self):
        print("Initialize Tower")
        super().__init__(400, 300, 'Images/player.PNG')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 250
        self.health = 1000

    def update(self):
        print("Update Tower")