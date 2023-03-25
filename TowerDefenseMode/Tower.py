from GameObject import GameObject
import pygame

class Tower(GameObject):
    def __init__(self, screen, health):
        print("Initialize Tower")

        super().__init__(400, 300, 'Images/towerDefense/td_castle.png')
        self.image = pygame.transform.scale(self.image, (200,200))

        self.rect = self.image.get_rect()
        self.rect.center = (500, 350)
        self.health = health
        self.screen = screen

    def update(self):
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(10,10,self.health/2, 20))

    def inflictDamage(self, damage):
        self.health -= damage