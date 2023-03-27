import math
import pygame
from GameObject import GameObject


class Cannonball(GameObject):
    def __init__(self, damage, direction, speed, x, y, imgPath, enemy, range):
        super().__init__(x,y,imgPath)

        self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.damage = damage
        self.direction = direction
        self.speed = speed
        self.referenceX = x
        self.referenceY = y
        self.xPos = x
        self.yPos = y
        self.targetEnemy = enemy
        self.range = range

    def update(self):
        self.move()
        self.registerCollision()

    def move(self):
        if(math.hypot(self.xPos - self.referenceX, self.yPos - self.referenceY) < self.range):
            self.xPos += self.direction[0] * self.speed
            self.yPos += self.direction[1] * self.speed
            self.rect.x = self.xPos
            self.rect.y = self.yPos
        else:
            self.kill()

    def registerCollision(self):
        if pygame.sprite.collide_rect(self, self.targetEnemy):
            self.targetEnemy.inflictDamage(self.damage)
            self.kill()