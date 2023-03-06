from ExplorationMode.Level import Level
import TowerDefenseMode.Exterior as Exterior
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
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
