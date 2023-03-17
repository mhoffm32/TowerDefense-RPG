from ExplorationMode.Player import Player
from ExplorationMode.SubArea.SubArea import SubArea
import pygame

class Level:
    def __init__(self, screen, progressBar):
        print("Initialize Level")
        self.screen = screen
        self.room = SubArea(0, self.screen, progressBar)

    def update(self):
        self.room.update()


