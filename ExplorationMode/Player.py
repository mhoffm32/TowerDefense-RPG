import sys

sys.path.append('../groupproject-team-99')

from Character import Character

import pygame

class Player(Character):
    def __init__(self,name,gender,skin_colour,hair_colour, screen, room, progressBar):
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
        self.progressBar = progressBar

        self.gender = gender

        self.skin_colour_images = {
            'light': pygame.image.load('Images\\boy\\skin\\forward\\boy_light_skin_forward.png').convert_alpha(),
            'medium': pygame.image.load('Images\\boy\\skin\\forward\\boy_medium_skin_forward.png').convert_alpha(),
            'dark': pygame.image.load('Images\\boy\\skin\\forward\\boy_dark_skin_forward.png').convert_alpha()
        }
        self.hair_colour_images = {
            'blonde': pygame.image.load('Images\\boy\hair\\forward\\boy_blonde_hair_forward.png').convert_alpha(),
            'brown': pygame.image.load('Images\\boy\hair\\forward\\boy_brown_hair_forward.png').convert_alpha(),
            'black': pygame.image.load('Images\\boy\hair\\forward\\boy_black_hair_forward.png').convert_alpha()
        }
    

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

    def update_skin(self,skin_colour):
        self.skin_colour_images[skin_colour] = pygame.transform.scale(self.skin_colour_images[skin_colour], (self.rect.width,self.rect.height))
        self.image.blit(self.skin_colour_images[skin_colour], (0,0))
        self.image = pygame.transform.scale(self.image, (self.rect.width,self.rect.height))

    def update_hair(self,hair_colour):
        self.hair_colour_images[hair_colour] = pygame.transform.scale(self.hair_colour_images[hair_colour],(self.rect.width,self.rect.height))
        self.image.blit(self.hair_colour_images[hair_colour],(0,0))
        self.image = pygame.transform.scale(self.image, (self.rect.width,self.rect.height))

    def collectItem(self, item):
        self.progressBar.add_coin(item.moneyValue)
        self.progressBar.add_diamond(item.crystalValue)

    #here we can add customizable features with different img urls for 
    #different characters depending on gender, hair color, etc'''
    #'''customizable name that we can use throughout the game'''



