import math
import pygame
from TowerDefenseMode.Troop import Troop
from TowerDefenseMode.Bolt import Bolt

class Ballista(Troop):
    def __init__(self,towerDefenseController, screen, slotNumber,attackSpeed, projectileHealth):
        img_path = 'Images/weapons/balista_sprite_left.png'
        super().__init__(0, 0,20,20, img_path)
        self.lastAttackTime = pygame.time.get_ticks()
        self.attackSpeed = attackSpeed                               # in millis
        self.arrowGroup = pygame.sprite.Group()
        self.towerDefenseController = towerDefenseController
        self.screen = screen
        self.projectileHealth = projectileHealth
        self.setPosition(slotNumber)
        self.rect.center = (self.rect.x, self.rect.y)

    def update(self):
        self.attack()
        self.arrowGroup.update()
        self.arrowGroup.draw(self.screen)

    def attack(self):
        if int(pygame.time.get_ticks() - self.lastAttackTime)%(self.attackSpeed) == 0:
            self.lastAttackTime = pygame.time.get_ticks()
            nearestEnemy = self.towerDefenseController.findNearestEnemy(self.rect.x, self.rect.y)
            enemyGroup = self.towerDefenseController.enemyGroup

            arrowDirection = [(nearestEnemy.rect.x - self.rect.x), (nearestEnemy.rect.y - self.rect.y)]
            directionMagnitude = math.sqrt((arrowDirection[0] * arrowDirection[0]) + (arrowDirection[1] * arrowDirection[1]))
            arrowDirection[0] = arrowDirection[0]/directionMagnitude
            arrowDirection[1] = arrowDirection[1]/directionMagnitude

            self.arrowGroup.add(Bolt(arrowDirection, .5, self.rect.x, self.rect.y, 'Images/weapons/arrow_sprite.png', enemyGroup, self.projectileHealth))