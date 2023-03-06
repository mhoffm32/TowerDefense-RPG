from ExplorationMode.SubArea.Wall import Wall
import pygame

class SubArea:
    def __init__(self, roomNumber, screen):
        print("Initialize Sub Area")
        self.wallGroup = pygame.sprite.Group()
        self.generateRoom(roomNumber)
        self.screen = screen

    def update(self):
        self.wallGroup.draw(self.screen)

    def generateRoom(self, roomNumber):
        print("Generate Room #" + str(roomNumber))
        if roomNumber == 0:
            print("Room 0")
            self.wallGroup.add(Wall(400,15,800,30))
            self.wallGroup.add(Wall(15,300,30,600))
            self.wallGroup.add(Wall(785,300,30,600))
            self.wallGroup.add(Wall(400, 585, 800,30))

    def checkCollision(self, player):
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        collisionDictionary = pygame.sprite.groupcollide(playerGroup, self.wallGroup, False, False)
        if len(collisionDictionary) > 0:
            return True

