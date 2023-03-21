import pygame
import time

import ProgressBar
from TestIntroCutscene import CutScene

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((1100, 800))
surface.fill((70, 9, 2))

# Initializing Color

pBar_group = pygame.sprite.Group([ProgressBar.ProgressBar(surface)])


# just to test what its like to pause with a moving background
myRect = pygame.Rect(300, 400, 300, 300)

# cutScene obj

introScene = CutScene(surface)


def homeUpdate():
    surface.fill((70, 9, 2))
    pygame.draw.rect(surface, (110, 74, 11), myRect)
    myRect.move_ip(1, 0)


def render(events):
    pBar_group.update(events)
    pygame.display.flip()
    pygame.display.update()


state = 1  # paused is 0

running = True

while running:

    events = pygame.event.get()

    for p in pBar_group:
        if p.paused:
            state = 0
        else:
            state = 1

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if state == 1:
        while(introScene.run):
            introScene.runScene()

        for event in events:
            if event.type == pygame.KEYDOWN:
                for p in pBar_group:
                    p.add_xp(5)

        render(events)
        homeUpdate()

    if state == 0:
        render(events)

    time.sleep(0.05)


# time.sleep(10)


pygame.quit()
