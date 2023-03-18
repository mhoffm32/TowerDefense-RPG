from ExplorationMode.SubArea.Wall import Wall
from ExplorationMode.SubArea.Door import Door
from ExplorationMode.SubArea.Item import Item
from ExplorationMode.Player import Player

import pygame

class SubArea:
    def __init__(self, roomNumber, screen, progressBar):
        print("Initialize Sub Area")
        self.roomNumber = roomNumber
        self.wallGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.itemGroup = pygame.sprite.Group()
        self.roomItemGroup = pygame.sprite.Group()
        self.generateItems()
        self.generateRoom(roomNumber)
        self.screen = screen

        self.playerGroup = pygame.sprite.Group()
        self.player = Player(0,0,0,0,screen, self, progressBar)
        self.playerGroup.add(self.player)

    def update(self):
        self.wallGroup.draw(self.screen)
        self.doorGroup.draw(self.screen)
        self.roomItemGroup.draw(self.screen)

        self.player.update()
        self.playerGroup.draw(self.screen)

    def generateRoom(self, roomNumber):
        self.roomNumber = roomNumber
        self.wallGroup.empty()
        self.doorGroup.empty()
        self.roomItemGroup.empty()
        if roomNumber == 0:
            self.wallGroup.add(Wall(15,450,35,700, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(985,450,35,700, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(500,100,1000,38, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(500, 685, 1000,38, 'Images\mapObjects\walls\800x30_wall.png'))
            

            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 1, [500,500]))

            for item in self.itemGroup:
                if item.room == roomNumber:
                    self.roomItemGroup.add(item)

        elif roomNumber == 1:
            self.wallGroup.add(Wall(15,450,35,700, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(985,450,35,700, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(500,100,1000,38, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(500, 685, 1000,38, 'Images\mapObjects\walls\800x30_wall.png'))

            self.wallGroup.add(Wall(800, 300, 1000,38, 'Images\mapObjects\walls\800x30_wall.png'))

            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 0, [500,200]))

            for item in self.itemGroup:
                if item.room == roomNumber:
                    self.roomItemGroup.add(item)

    def checkCollision(self):
        #Check Collision with Item
        keysPressed = pygame.key.get_pressed()
        if(keysPressed[pygame.K_f]):
            itemCollisionDictionary = pygame.sprite.groupcollide(self.itemGroup, self.playerGroup, False, False)
            for item in itemCollisionDictionary:
                if item.room == self.roomNumber:
                    self.player.collectItem(item)
                    self.itemGroup.remove(item)
                    self.roomItemGroup.remove(item)

        #Check Collision with Door
        doorCollisionDictionary = pygame.sprite.groupcollide(self.doorGroup, self.playerGroup, False, False)
        for door in doorCollisionDictionary:
            self.generateRoom(door.nextLevelNumber)
            self.player.setPosition(door.newRoomSpawnLocation)
            break

        #Check Collision with Wall
        wallCollisionDictionary = pygame.sprite.groupcollide(self.playerGroup, self.wallGroup, False, False)
        if len(wallCollisionDictionary) > 0:
            return True
        

    def get_player(self):
        return self.player

    def generateItems(self):
        self.itemGroup.add(Item(100, 0,0, 900,200,1, 'Images/coin.png'))
        self.itemGroup.add(Item(0, 1,0, 900,600,1, 'Images/Diamond.png'))
        self.itemGroup.add(Item(100, 0,0, 900,600,0, 'Images/coin.png'))


