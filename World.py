from ExplorationMode.Level import Level
import TowerDefenseMode.Exterior as Exterior
import pygame
from ExplorationMode.Player import Player
from ExplorationMode.SubArea.SubArea import SubArea
import ProgressBar
from TowerDefenseMode.TowerDefenseModeController import TowerDefenseModeController

pygame.init()

screen = pygame.display.set_mode((1000, 700))
screenRectangle = screen.get_rect()

# Progress Bar Stuff
progressBar = ProgressBar.ProgressBar(screen)
pBar_group = pygame.sprite.Group(progressBar)
level = Level(screen, progressBar)


def render(events):
    pBar_group.update(events)

    pygame.display.flip()
    pygame.display.update()


state = 1  # paused is 0

gameMode = 'explore'

tdController = TowerDefenseModeController(screen, progressBar)
bg = pygame.image.load('Images/towerDefense/td_background.png').convert()


running = True
progressBar.reset_timer(30)

while(running):

    events = pygame.event.get()

    for event in events:
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
                    p.update_xp(5)

    if gameMode == 'explore':
        level.update()
        pBar_group.update(events)

        if progressBar.attackMode:
            print("Entering TD Mode")
            gameMode = 'tdMode'
            defenderStats = {'archerDamage': 60, 'archerAttackSpeed': 2000, 'pikemanDamage': 90, 'pikemanAttackSpeed': 2000, 'ballistaAttackSpeed': 5000,
                             'ballistaProjectileHealth': 120, 'towerHealth': 700, 'cannonAttackSpeed': 6000, 'cannonDamage': 200, 'cannonRange': 200}
            tdController.generateDefenders(0, 0, 0, 20)
            tdController.generateWave()

        pygame.display.flip()
        screen.fill((0, 0, 0))

    elif gameMode == 'tdMode':
        tdController.update()
        if tdController.checkLost():
            print("Wave Lost")
            gameMode = 'explore'
            progressBar.reset_timer(20)
            progressBar.attackMode = False
            progressBar.update_xp(-15)
        elif tdController.checkWon():
            print("Wave Defeated")
            gameMode = 'explore'
            progressBar.reset_timer(90)
            progressBar.attackMode = False
            progressBar.add_xp(15)

        pygame.display.flip()
        screen.blit(bg, (0, 0))

pygame.quit()
