import math
import pygame
from TowerDefenseMode.Troop import Troop
from TowerDefenseMode.Cannonball import Cannonball


class Cannon(Troop):
    def __init__(self,towerDefenseController, screen, slotNumber, damage, attackSpeed, range):
        img_path = 'Images/weapons/cannons_sprite_left.png'
        super().__init__(0, 0,20,20, img_path)
        self.lastAttackTime = pygame.time.get_ticks()
        self.attackSpeed = attackSpeed                               # in millis
        self.cannonBallGroup = pygame.sprite.Group()
        self.towerDefenseController = towerDefenseController
        self.screen = screen
        self.damage = damage
        self.attackRange = range
        self.setPosition(slotNumber)
        self.rect.center = (self.rect.x, self.rect.y)

    def update(self):
        self.attack()
        self.cannonBallGroup.update()
        self.cannonBallGroup.draw(self.screen)

    def attack(self):
        if int(pygame.time.get_ticks() - self.lastAttackTime)%(self.attackSpeed) == 0:
            self.lastAttackTime = pygame.time.get_ticks()
            nearestEnemy = self.towerDefenseController.findNearestEnemy(self.rect.x, self.rect.y)

            if math.hypot(self.rect.x - nearestEnemy.rect.x, self.rect.y - nearestEnemy.rect.y) <= self.attackRange:
                projectileDirection = [(nearestEnemy.rect.x - self.rect.x), (nearestEnemy.rect.y - self.rect.y)]
                directionMagnitude = math.sqrt((projectileDirection[0] * projectileDirection[0]) + (projectileDirection[1] * projectileDirection[1]))
                projectileDirection[0] = projectileDirection[0]/directionMagnitude
                projectileDirection[1] = projectileDirection[1]/directionMagnitude

                self.cannonBallGroup.add(Cannonball(self.damage, projectileDirection, .25, self.rect.x, self.rect.y, 'Images/weapons/cannonball.PNG', nearestEnemy, self.attackRange))
