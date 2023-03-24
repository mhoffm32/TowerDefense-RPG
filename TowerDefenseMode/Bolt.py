#Basically an arrow but with some additional functionality for use with the Ballista

import pygame
from GameObject import GameObject

class Bolt(GameObject):
    def __init__(self, direction, speed, x, y, imgPath, enemyGroup, health):
        super().__init__(x,y,imgPath)
        self.direction = direction
        self.speed = speed
        self.xPos = x
        self.yPos = y
        self.enemyGroup = enemyGroup
        self.health = health

    def update(self):
        self.move()
        self.registerCollision()

    def move(self):
        self.xPos += self.direction[0] * self.speed
        self.yPos += self.direction[1] * self.speed
        self.rect.x = self.xPos
        self.rect.y = self.yPos

    def registerCollision(self):
        selfGroup = pygame.sprite.Group()
        selfGroup.add(self)
        collisionDictionary = pygame.sprite.groupcollide(self.enemyGroup, selfGroup, False, False)

        for enemy in collisionDictionary:
            damageInflicted = enemy.inflictDamage(self.health)
            self.health -= damageInflicted
            if self.health <= 0:
                self.kill()
                break