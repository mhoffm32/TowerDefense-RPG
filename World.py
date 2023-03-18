from ExplorationMode.Level import Level
import TowerDefenseMode.Exterior as Exterior
import pygame
from ExplorationMode.Player import Player
from ExplorationMode.SubArea.SubArea import SubArea

pygame.init()

screen = pygame.display.set_mode((1000,700))
screenRectangle = screen.get_rect()

level = Level(screen) 

running = True
while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.update()
    pygame.display.flip()
    screen.fill((0,0,0))

pygame.quit()
