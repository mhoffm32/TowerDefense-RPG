from ExplorationMode.Player import Player
from ExplorationMode.SubArea.SubArea import SubArea
import pygame

class Level:
    def __init__(self, screen, progressBar,player):
        print("Initialize Level")
        self.screen = screen
        self.player = player
        self.room = SubArea(0, self.screen, progressBar,self.player)

    def update(self):
        self.room.update()


