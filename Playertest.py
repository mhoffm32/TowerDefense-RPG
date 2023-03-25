from ExplorationMode.Player import Player
from ProgressBar import ProgressBar
import pygame


screen = pygame.display.set_mode((1000, 800))
pBar = ProgressBar(screen)

gamePlayer = Player(screen, pBar)

gamePlayer.getPlayerMenu()
