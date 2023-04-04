from ExplorationMode.Level import Level
import pygame
from ExplorationMode.Player import Player
from ExplorationMode.SubArea.SubArea import SubArea
import ProgressBar
from TowerDefenseMode.TowerDefenseModeController import TowerDefenseModeController
from TestIntroCutscene import CutScene
from BadEndingCutscene import BadCutscene
from GoodEndingCutscene import GoodCutscene
from SecretEndingCutscene import SecretCutscene
from Instructions import Instructions
import random

pygame.init()
screen = pygame.display.set_mode((1000, 700))
screenRectangle = screen.get_rect()

# Progress Bar Stuff
progressBar = ProgressBar.ProgressBar(screen)
pBar_group = pygame.sprite.Group(progressBar)

def render(events):
    pBar_group.update(events)

    pygame.display.flip()
    pygame.display.update()

state = 1  # paused is 0

instructionScene = Instructions(screen)
instructionScene.runScene()
introScene = CutScene(screen)
introScene.runScene()

temp_player = Player(screen, progressBar, 400, 600)
game_player = temp_player.customize()

game_playerG = pygame.sprite.Group([game_player])

store = SubArea(6, screen, progressBar, game_player)
level = Level(screen, progressBar, game_player)

tdController = TowerDefenseModeController(screen, progressBar)
bg = pygame.image.load('Images/towerDefense/td_background.png').convert()

win = False
lose = False
secret = False

progressBar.reset_timer(60)
gameMode = "explore"

running = True

while(running):

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    for p in pBar_group:
        if p.win:
            win = True
            running = False
        elif p.lose:
            lose = True
            running = False
        elif p.secret:
            secret = True
            running = False

        if p.paused:
            state = 0
        else:
            state = 1

    if gameMode == 'explore':
        level.update()
        pBar_group.update(events)

        if progressBar.attackMode:
            print("Entering TD Mode")
            gameMode = 'tdMode'
            tdController.generateDefenders(random.randint(1,3), random.randint(1,2), random.randint(1,4), random.randint(10,15))
            tdController.generateWave()

        pygame.display.flip()
        screen.fill((0, 0, 0))

    elif gameMode == 'tdMode':
        tdController.update()
        if tdController.checkLost():
            print("Wave Lost")
            gameMode = 'explore'
            progressBar.reset_timer(60)
            progressBar.attackMode = False
            progressBar.update_xp(-10)

        elif tdController.checkWon():
            print("Wave Defeated")
            gameMode = 'explore'
            progressBar.reset_timer(60)
            progressBar.attackMode = False
            progressBar.update_xp(10)

        pygame.display.flip()
        screen.blit(bg, (0, 0))

    elif gameMode == "store":
        store.update()
        pBar_group.update(events)
        pygame.display.flip()
        screen.fill((0, 0, 0))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    for p in pBar_group:
                        p.attackMode = True
                        gameMode = 'explore'

if lose:
    BadCutscene().run()
elif win:
    GoodCutscene().run()
elif secret:
    SecretCutscene().run()

pygame.quit()
