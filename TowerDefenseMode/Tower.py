from GameObject import GameObject
import pygame

class Tower(GameObject):
    def __init__(self, screen):
        print("Initialize Tower")
        super().__init__(400, 300, 'Images/player.PNG')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 250
        self.health = 1000
        self.screen = screen

    def update(self):
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(10,10,self.health/2, 20))

    def inflictDamage(self, damage):
        self.health -= damage