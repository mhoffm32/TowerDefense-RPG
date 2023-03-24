import math
import pygame
from TowerDefenseMode.Troop import Troop


class Pikeman(Troop):
    def __init__(self,screen, towerDefenseController, slotNumber, damage, attackSpeed):
        img_path = 'Images/weapons/pikeman_left_idle_sprite.png'
        super().__init__(0, 0,50,50, img_path)
        self.lastAttackTime = pygame.time.get_ticks()
        self.attackSpeed = 2000                               # in millis
        self.arrowGroup = pygame.sprite.Group()
        self.towerDefenseController = towerDefenseController
        self.screen = screen
        self.damage = damage
        self.attackRange = 50
        self.setPosition(slotNumber)
        self.rect.center = (self.rect.x, self.rect.y)

    def update(self):
        self.attack()

    def attack(self):
        if int(pygame.time.get_ticks() - self.lastAttackTime)%(self.attackSpeed) == 0:
            self.lastAttackTime = pygame.time.get_ticks()
            nearestEnemy = self.towerDefenseController.findNearestEnemy(self.rect.x, self.rect.y)

            print(str(math.hypot(self.rect.x - nearestEnemy.rect.x, self.rect.y - nearestEnemy.rect.y)))

            if math.hypot(self.rect.x - nearestEnemy.rect.x, self.rect.y - nearestEnemy.rect.y) <= self.attackRange:
                nearestEnemy.inflictDamage(self.damage)


    #print("initialize Pikeman")
