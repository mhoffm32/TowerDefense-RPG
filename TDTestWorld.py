import pygame
import threading

from TowerDefenseMode.TowerDefenseModeController import TowerDefenseModeController

pygame.init()

screen = pygame.display.set_mode((1000,700))
screenRectangle = screen.get_rect()

bg = pygame.image.load('Images/towerDefense/td_background.png').convert()


tdController = TowerDefenseModeController(screen)


running = True
while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tdController.update()
    pygame.display.flip()
    screen.blit(bg,(0,0))

pygame.quit()