import sys

sys.path.append('../se2250groupproject')

from Character import Character

import pygame

class Player(Character):
    def __init__(self,name,gender,hair_color, screen, room):
        print("Initialize Player")
        super().__init__(500,500,'Images\\boy\\boy_mannequin_forward_idle.png')
        self.speed = 1
        self.screen = screen
        self.room = room

    def update(self):
        self.move()

    def move(self):
        # loading sprite images to change depending on character movement
        sideSprite = pygame.image.load('Images\\boy\\boy_mannequin_side_idle.png')
        downSprite = pygame.image.load('Images\\boy\\boy_mannequin_forward_idle.png')
        upSprite = pygame.image.load('Images\\boy\\boy_mannequin_back_idle.png')
        # move the player
        keysPressed = pygame.key.get_pressed()
        if(keysPressed[pygame.K_LEFT]):
            print("Move Left")
            self.rect.x -= self.speed

            self.image = sideSprite
            self.image = pygame.transform.flip(self.image,True,False)
        if(keysPressed[pygame.K_RIGHT]):
            print("Move Right")
            self.rect.x += self.speed

            self.image = sideSprite
        if(keysPressed[pygame.K_UP]):
            print("Move UP")
            self.rect.y -= self.speed

            self.image = upSprite
        if(keysPressed[pygame.K_DOWN]):
            print("Move Down")
            self.rect.y += self.speed

            self.image = downSprite

        # if the result of the move puts the player in a wall: revert movement
        if self.room.checkCollision(self):
            if(keysPressed[pygame.K_LEFT]):
                print("Move Left")
                self.rect.x += self.speed
            if(keysPressed[pygame.K_RIGHT]):
                print("Move Right")
                self.rect.x -= self.speed
            if(keysPressed[pygame.K_UP]):
                print("Move UP")
                self.rect.y += self.speed
            if(keysPressed[pygame.K_DOWN]):
                print("Move Down")
                self.rect.y -= self.speed

        

    #here we can add customizable features with different img urls for 
    #different characters depending on gender, hair color, etc'''
    #'''customizable name that we can use throughout the game'''



