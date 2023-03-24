import math

import pygame
from TowerDefenseMode.Troop import Troop
from TowerDefenseMode.Arrow import Arrow


class Archer(Troop):
    def __init__(self, towerDefenseController, screen, slotNumber):
        img_path = 'Images/weapons/bow_arrow_sprite.png'
        super().__init__(0, 0,20,20, img_path)
        self.lastAttackTime = pygame.time.get_ticks()
        self.attackSpeed = 2000                               # in millis
        self.arrowGroup = pygame.sprite.Group()
        self.towerDefenseController = towerDefenseController
        self.screen = screen
        self.damage = 60
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

            arrowDirection = [(nearestEnemy.rect.x - self.rect.x), (nearestEnemy.rect.y - self.rect.y)]
            directionMagnitude = math.sqrt((arrowDirection[0] * arrowDirection[0]) + (arrowDirection[1] * arrowDirection[1]))
            arrowDirection[0] = arrowDirection[0]/directionMagnitude
            arrowDirection[1] = arrowDirection[1]/directionMagnitude

            self.arrowGroup.add(Arrow(self.damage, arrowDirection, .5, self.rect.x, self.rect.y, 'Images/weapons/arrow_sprite.png', nearestEnemy))
    
    