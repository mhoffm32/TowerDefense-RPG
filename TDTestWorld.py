import pygame
import threading

from TowerDefenseMode.TowerDefenseModeController import TowerDefenseModeController

pygame.init()

screen = pygame.display.set_mode((1000,700))
screenRectangle = screen.get_rect()

tdController = TowerDefenseModeController(screen)

running = True
while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tdController.update()
    pygame.display.flip()
    screen.fill((0,0,0))



pygame.quit()