from ExplorationMode.SubArea.Obstacle import Obstacle
import pygame


class Door(Obstacle):
    def __init__(self, x, y, imgPath, nextLevelNumber, newRoomSpawnLocation):
        super().__init__(x, y, imgPath)

        self.nextLevelNumber = nextLevelNumber
        self.newRoomSpawnLocation = newRoomSpawnLocation

        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = (y-(self.rect.height/4))

