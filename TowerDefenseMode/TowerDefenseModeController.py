import pygame
import sys
import random

sys.path.append('../se2250groupproject')
from TowerDefenseMode.Enemy1 import Enemy1
from TowerDefenseMode.Enemy import Enemy
from TowerDefenseMode.Enemy2 import Enemy2
from TowerDefenseMode.Enemy3 import Enemy3
from TowerDefenseMode.Tower import Tower
from TowerDefenseMode.Archer import Archer
from TowerDefenseMode.Pikeman import Pikeman
from TowerDefenseMode.Ballista import Ballista

class TowerDefenseModeController:
    def __init__(self, screen):
        self.screen = screen
        self.waveNumber = 1

        self.towerGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.defenderGroup = pygame.sprite.Group()

    def update(self):
        self.towerGroup.draw(self.screen)
        self.enemyGroup.draw(self.screen)
        self.defenderGroup.draw(self.screen)

        self.enemyGroup.update()
        self.towerGroup.update()
        self.defenderGroup.update()


    def findNearestEnemy(self, archerX, archerY):
        closestEnemy = Enemy(-1000,-1000,'Images/boy/boy_mannequin_back_idle.png',self.tower, 20, 20)
        distance = 2000
        for e in self.enemyGroup:
            pos = pygame.math.Vector2(archerX, archerY)
            currentDist = pos.distance_to(pygame.math.Vector2(e.rect.x, e.rect.y))
            if(currentDist < distance):
                closestEnemy = e
                distance = currentDist

        return closestEnemy

    def generateDefenders(self, numOfArchers, numOfPikeman, numOfBallista, numOfCannon, defenderStats):
        self.defenderGroup.empty()
        slotNumber = 0

        self.towerGroup.empty()
        self.tower = Tower(self.screen, defenderStats['towerHealth'])
        self.towerGroup.add(self.tower)

        for i in range(0,numOfPikeman):
            self.defenderGroup.add(Pikeman(self.screen,self, slotNumber, defenderStats['pikemanDamage'], defenderStats['pikemanAttackSpeed']))
            slotNumber += 1

        for i in range(0,numOfArchers):
            self.defenderGroup.add(Archer(self, self.screen, slotNumber, defenderStats['archerDamage'], defenderStats['archerAttackSpeed']))
            slotNumber += 1

        for i in range(0,numOfBallista):
            self.defenderGroup.add(Ballista(self, self.screen, slotNumber, defenderStats['ballistaAttackSpeed'], defenderStats['ballistaProjectileHealth']))
            slotNumber += 1

    def generateWave(self):
        for i in range(0,self.waveNumber + 2):
            sector = random.randint(0,3)
            if sector == 0:  #sector zero will be the top of the screen
                self.enemyGroup.add(Enemy(random.randint(20,780),20,'Images/boy/boy_mannequin_back_idle.png',self.tower, 20, 20))

            elif sector == 1:  #sector zero will be the right of the screen
                self.enemyGroup.add(Enemy(780,random.randint(20,580),'Images/boy/boy_mannequin_back_idle.png',self.tower, 20, 20))

            elif sector == 2:  #sector zero will be the bottom of the screen
                self.enemyGroup.add(Enemy(random.randint(20,780),580,'Images/boy/boy_mannequin_back_idle.png',self.tower, 20, 20))

            else:  #sector 3 will be the left of the screen
                self.enemyGroup.add(Enemy(20,random.randint(20,580),'Images/boy/boy_mannequin_back_idle.png',self.tower, 20, 20))

        for i in range(0, (self.waveNumber - 2)*2):
            sector = random.randint(0,3)
            if sector == 0:  #sector zero will be the top of the screen
                self.enemyGroup.add(Enemy1(random.randint(20,780),20,'Images/girl/girl_mannequin_forward.png',self.tower))

            elif sector == 1:  #sector zero will be the right of the screen
                self.enemyGroup.add(Enemy1(780,random.randint(20,580),'Images/girl/girl_mannequin_forward.png',self.tower))

            elif sector == 2:  #sector zero will be the bottom of the screen
                self.enemyGroup.add(Enemy1(random.randint(20,780),580,'Images/girl/girl_mannequin_forward.png',self.tower))

            else:  #sector 3 will be the left of the screen
                self.enemyGroup.add(Enemy1(20,random.randint(20,580),'Images/girl/girl_mannequin_forward.png',self.tower))

        for i in range(0, (self.waveNumber - 3)):
            sector = random.randint(0,3)
            if sector == 0:  #sector zero will be the top of the screen
                self.enemyGroup.add(Enemy2(random.randint(20,780),20,'Images/weapons/pikeman_right_idle_sprite.png',self.tower))

            elif sector == 1:  #sector zero will be the right of the screen
                self.enemyGroup.add(Enemy2(780,random.randint(20,580),'Images/weapons/pikeman_right_idle_sprite.png',self.tower))

            elif sector == 2:  #sector zero will be the bottom of the screen
                self.enemyGroup.add(Enemy2(random.randint(20,780),580,'Images/weapons/pikeman_right_idle_sprite.png',self.tower))

            else:  #sector 3 will be the left of the screen
                self.enemyGroup.add(Enemy2(20,random.randint(20,580),'Images/weapons/pikeman_right_idle_sprite.png',self.tower))

        for i in range(0, (self.waveNumber - 3)):
            sector = random.randint(0,3)
            if sector == 0:  #sector zero will be the top of the screen
                self.enemyGroup.add(Enemy3(random.randint(20,780),20,'Images/boy/boy_mannequin_back_idle.png',self.tower))

            elif sector == 1:  #sector zero will be the right of the screen
                self.enemyGroup.add(Enemy3(780,random.randint(20,580),'Images/boy/boy_mannequin_back_idle.png',self.tower))

            elif sector == 2:  #sector zero will be the bottom of the screen
                self.enemyGroup.add(Enemy3(random.randint(20,780),580,'Images/boy/boy_mannequin_back_idle.png',self.tower))

            else:  #sector 3 will be the left of the screen
                self.enemyGroup.add(Enemy3(20,random.randint(20,580),'Images/boy/boy_mannequin_back_idle.png',self.tower))

    def checkWon(self):
        if (len(self.enemyGroup) <= 0):
            self.waveNumber += 1
            return True
        
    
