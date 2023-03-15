import pygame
import sys
import random

sys.path.append('../se2250groupproject')
from TowerDefenseMode.Enemy1 import Enemy1
from TowerDefenseMode.Tower import Tower

class TowerDefenseModeController:
    def __init__(self, screen):
        print("Initialize TowerDefenseMode")
        self.screen = screen
        self.towerGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.generateWave(0)

    def update(self):
        self.towerGroup.draw(self.screen)
        self.enemyGroup.draw(self.screen)

        self.enemyGroup.update()

    def generateWave(self, waveNumber):
        print("Generate Wave #" + str(waveNumber))
        self.towerGroup.add(Tower())
        for i in range(0,waveNumber + 2):
            #self.enemyGroup.add(Enemy1(i*100,250,'Images/wall30x600.PNG'))
            sector = random.randint(0,3)
            if sector == 0:  #sector zero will be the top of the screen
                self.enemyGroup.add(Enemy1(random.randint(20,780),20,'Images/wall30x600.PNG'))

            elif sector == 1:  #sector zero will be the right of the screen
                self.enemyGroup.add(Enemy1(780,random.randint(20,580),'Images/wall30x600.PNG'))

            elif sector == 2:  #sector zero will be the bottom of the screen
                self.enemyGroup.add(Enemy1(random.randint(20,780),580,'Images/wall30x600.PNG'))

            else:  #sector 3 will be the left of the screen
                self.enemyGroup.add(Enemy1(20,random.randint(20,580),'Images/wall30x600.PNG'))
