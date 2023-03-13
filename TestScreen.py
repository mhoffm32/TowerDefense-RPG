import pygame
import time

import ProgressBar

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((1100, 800))
surface.fill((70, 9, 2))

# Initializing Color

pBar_group = pygame.sprite.Group([ProgressBar.ProgressBar(surface)])


def render(events):
    pBar_group.update(events)

    pygame.display.flip()
    pygame.display.update()


running = True

while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            for p in pBar_group:
                p.add_xp(5)

    render(events)
    time.sleep(0.05)


# time.sleep(10)


pygame.quit()
