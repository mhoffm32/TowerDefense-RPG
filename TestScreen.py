import pygame
import time

from ExplorationMode.Player import Player
import ProgressBar
from TestIntroCutscene import CutScene

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((1100, 800))
surface.fill((153, 204, 255))

# Initializing Color

prog = ProgressBar.ProgressBar(surface)

pBar_group = pygame.sprite.Group([prog])
prog.reset_timer(180)


# just to test what its like to pause with a moving background
myRect = pygame.Rect(300, 400, 300, 300)
temp_player = Player(surface, prog, 400, 600)

# cutScene obj

introScene = CutScene(surface)


def homeUpdate():
    surface.fill((120, 180, 240))
    #pygame.draw.rect(surface, (110, 74, 11), myRect)
    #myRect.move_ip(1, 0)


def render(events):
    pBar_group.update(events)
    pygame.display.flip()
    pygame.display.update()


# introScene.runScene()
gamePlayer = temp_player.customize()

gamePlayer_G = pygame.sprite.Group([gamePlayer])

state = 1  # paused is 0

running = True

while running:

    events = pygame.event.get()

    for p in pBar_group:
        if p.paused:
            state = 0
        else:
            state = 1

    gamePlayer_G.draw(surface)

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.WINDOWSHOWN:
            for p in pBar_group:
                p.reset_timer(180)

    if state == 1:

        gamePlayer_G.update()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    for p in pBar_group:
                        p.reset_timer(180)

        render(events)
        homeUpdate()

    if state == 0:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    for p in pBar_group:
                        p.paused = False

        render(events)

    time.sleep(0.05)


# time.sleep(10)


pygame.quit()
