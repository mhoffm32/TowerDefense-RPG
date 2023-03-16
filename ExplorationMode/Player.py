import sys

sys.path.append('../groupproject-team-99')

from Character import Character

import pygame

class Player(Character):
    def __init__(self,name,gender,hair_color, screen, room):
        super().__init__(500,500,'Images\\boy\\boy_mannequin_forward_idle.png')

        self.image = pygame.transform.scale(self.image, (50,70))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300

        self.sideSprite = pygame.image.load('Images\\boy\\boy_mannequin_side_idle.png')
        self.downSprite = pygame.image.load('Images\\boy\\boy_mannequin_forward_idle.png')
        self.upSprite = pygame.image.load('Images\\boy\\boy_mannequin_back_idle.png')
        self.sideSprite = pygame.transform.scale(self.sideSprite, (50,70))
        self.downSprite = pygame.transform.scale(self.downSprite, (50,70))
        self.upSprite = pygame.transform.scale(self.upSprite, (50,70))

        self.speed = 1
        self.screen = screen
        self.room = room

    def update(self):
        self.move()

    def setPosition(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def move(self):
        # loading sprite images to change depending on character movement

        # move the player
        keysPressed = pygame.key.get_pressed()
        if(keysPressed[pygame.K_LEFT]):
            self.rect.x -= self.speed

            self.image = self.sideSprite
            self.image = pygame.transform.flip(self.image,True,False)
        if(keysPressed[pygame.K_RIGHT]):
            self.rect.x += self.speed

            self.image = self.sideSprite
        if(keysPressed[pygame.K_UP]):
            self.rect.y -= self.speed

            self.image = self.upSprite
        if(keysPressed[pygame.K_DOWN]):
            self.rect.y += self.speed

            self.image = self.downSprite

        # if the result of the move puts the player in a wall: revert movement
        if self.room.checkCollision():
            if(keysPressed[pygame.K_LEFT]):
                self.rect.x += self.speed
            if(keysPressed[pygame.K_RIGHT]):
                self.rect.x -= self.speed
            if(keysPressed[pygame.K_UP]):
                self.rect.y += self.speed
            if(keysPressed[pygame.K_DOWN]):
                self.rect.y -= self.speed

        

    #here we can add customizable features with different img urls for 
    #different characters depending on gender, hair color, etc'''
    #'''customizable name that we can use throughout the game'''



