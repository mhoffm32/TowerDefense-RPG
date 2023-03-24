import math
import time
from Character import Character
import pygame
import threading


class Enemy(Character, threading.Thread):
    def __init__(self, x, y, img_path, tower):
        # initialize other enemy specific attributes
        super().__init__(x, y, img_path)
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = self.getDirection()
        self.speed = .05                        #Should be overwritten in Child Class
        self.xPos = x
        self.yPos = y
        self.reachedTower = False
        self.tower = tower
        self.damage = 10
        self.attackSpeed = 2                    #in Seconds
        self.lastAttackTime = time.time()
        self.dead = False
        self.health = 100

    def update(self):
        self.move()
        self.attack()

    def getDirection(self):
        directionX = 500 - self.rect.x
        directionY = 350 - self.rect.y
        directionMagnitude = math.sqrt((directionX * directionX) + (directionY * directionY))
        direction = (directionX/directionMagnitude, directionY/directionMagnitude)
        return direction
    
    def move(self):
        #rect.x and rect.y can only store ints because they represent which pixel it is located at on the screen
        #there obviously can't be any partial pixels. Therefore we create a new variable which CAN hold floats
        #this way we can reduce the speed to less than a pixel a second

        if not self.reachedTower:
            self.xPos = self.xPos + (self.direction[0] * self.speed)
            self.yPos = self.yPos + (self.direction[1] * self.speed)
            self.rect.x = self.xPos
            self.rect.y = self.yPos

        self.reachedTower = pygame.sprite.collide_rect(self, self.tower)

    def attack(self):

        if self.reachedTower and (int(time.time()*1000 - self.lastAttackTime)%(self.attackSpeed*1000) == 0):
            self.tower.inflictDamage(self.damage)
            self.lastAttackTime = time.time()*1000

    def inflictDamage(self, damage):
        self.health -= damage
        self.checkAlive()

    def checkAlive(self):
        if self.health <= 0:
            self.kill()


