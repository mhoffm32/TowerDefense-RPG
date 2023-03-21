from ExplorationMode.Level import Level
import TowerDefenseMode.Exterior as Exterior
import pygame
from ExplorationMode.Player import Player
from ExplorationMode.SubArea.SubArea import SubArea
import ProgressBar

pygame.init()

screen = pygame.display.set_mode((1000,700))
screenRectangle = screen.get_rect()

#Progress Bar Stuff
progressBar = ProgressBar.ProgressBar(screen)
pBar_group = pygame.sprite.Group(progressBar)
level = Level(screen, progressBar)

def render(events):
    pBar_group.update(events)

    pygame.display.flip()
    pygame.display.update()

state = 1  # paused is 0              

running = True
while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for p in pBar_group:
        if p.paused:
            state = 0
        else:
            state = 1

    if state == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                for p in pBar_group:
                    p.add_xp(5)

    level.update()
    pBar_group.update(pygame.event.get())
    pygame.display.flip()
    screen.fill((0,0,0))

pygame.quit()
