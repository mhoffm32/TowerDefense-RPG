from ExplorationMode.Player import Player
from ExplorationMode.SubArea.SubArea import SubArea
import pygame

class Level:
    def __init__(self, screen):
        print("Initialize Level")
        self.screen = screen
        self.playerGroup = pygame.sprite.Group()
        self.room = SubArea(0, self.screen)
        self.player = Player(0,0,0,screen, self.room)
        self.playerGroup.add(self.player)

    def update(self):
        self.player.update()
        self.playerGroup.draw(self.screen)

        self.room.update()


