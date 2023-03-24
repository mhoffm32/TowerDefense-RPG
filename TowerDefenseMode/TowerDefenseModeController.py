import pygame
import sys
import random

sys.path.append('../se2250groupproject')
from TowerDefenseMode.Enemy1 import Enemy1
from TowerDefenseMode.Tower import Tower
from TowerDefenseMode.Archer import Archer
from TowerDefenseMode.Pikeman import Pikeman

class TowerDefenseModeController:
    def __init__(self, screen):
        self.screen = screen
        self.towerGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.defenderGroup = pygame.sprite.Group()
        self.tower = Tower(self.screen)
        self.towerGroup.add(self.tower)
        self.generateDefenders(0,0,0,0)
        self.generateWave(0)

    def update(self):
        self.towerGroup.draw(self.screen)
        self.enemyGroup.draw(self.screen)
        self.defenderGroup.draw(self.screen)

        self.enemyGroup.update()
        self.towerGroup.update()
        self.defenderGroup.update()


    def findNearestEnemy(self, archerX, archerY):
        closestEnemy = 0
        distance = 2000
        for e in self.enemyGroup:
            pos = pygame.math.Vector2(archerX, archerY)
            currentDist = pos.distance_to(pygame.math.Vector2(e.rect.x, e.rect.y))
            if(currentDist < distance):
                closestEnemy = e
                distance = currentDist

        return closestEnemy

    def generateDefenders(self, numOfArchers, numOfPikeman, numOfBallista, numOfCannon):
        self.defenderGroup.empty()
        slotNumber = 0

        numOfArchers = 10
        numOfPikeman = 10

        for i in range(0,numOfPikeman):
            self.defenderGroup.add(Pikeman(self.screen,self, slotNumber))
            slotNumber += 1

        for i in range(0,numOfArchers):
            self.defenderGroup.add(Archer(self, self.screen, slotNumber))
            slotNumber += 1

    def generateWave(self, waveNumber):
        for i in range(0,waveNumber + 2):
            #self.enemyGroup.add(Enemy1(i*100,250,'Images/wall30x600.PNG'))
            sector = random.randint(0,3)
            if sector == 0:  #sector zero will be the top of the screen
                self.enemyGroup.add(Enemy1(random.randint(20,780),20,'Images/wall30x600.PNG',self.tower))

            elif sector == 1:  #sector zero will be the right of the screen
                self.enemyGroup.add(Enemy1(780,random.randint(20,580),'Images/wall30x600.PNG',self.tower))

            elif sector == 2:  #sector zero will be the bottom of the screen
                self.enemyGroup.add(Enemy1(random.randint(20,780),580,'Images/wall30x600.PNG',self.tower))

            else:  #sector 3 will be the left of the screen
                self.enemyGroup.add(Enemy1(20,random.randint(20,580),'Images/wall30x600.PNG',self.tower))

    def checkWon(self):
        return (len(self.enemyGroup) <= 0)
