from ExplorationMode.SubArea.Wall import Wall
from ExplorationMode.SubArea.Door import Door
from ExplorationMode.Player import Player
import pygame

class SubArea:
    def __init__(self, roomNumber, screen):
        print("Initialize Sub Area")
        self.wallGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.generateRoom(roomNumber)
        self.screen = screen

        self.playerGroup = pygame.sprite.Group()
        self.player = Player(0,0,0,0,screen, self)
        self.playerGroup.add(self.player)

    def update(self):
        self.wallGroup.draw(self.screen)
        self.doorGroup.draw(self.screen)

        self.player.update()
        self.playerGroup.draw(self.screen)

    def generateRoom(self, roomNumber):
        self.wallGroup.empty()
        self.doorGroup.empty()
        if roomNumber == 0:
            self.wallGroup.add(Wall(15,450,35,700, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(985,450,35,700, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(500,100,1000,38, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(500, 685, 1000,38, 'Images\mapObjects\walls\800x30_wall.png'))
            

            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 1, [500,500]))
        if roomNumber == 1:
            self.wallGroup.add(Wall(15,450,35,700, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(985,450,35,700, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(500,100,1000,38, 'Images\mapObjects\walls\800x30_wall.png'))
            self.wallGroup.add(Wall(500, 685, 1000,38, 'Images\mapObjects\walls\800x30_wall.png'))

            self.wallGroup.add(Wall(800, 300, 1000,38, 'Images\mapObjects\walls\800x30_wall.png'))

            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 0, [500,200]))

    def checkCollision(self, player):
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)

        #Check Collision with Door
        doorCollisionDictionary = pygame.sprite.groupcollide(self.doorGroup, playerGroup, False, False)
        for door in doorCollisionDictionary:
            self.generateRoom(door.nextLevelNumber)
            self.player.setPosition(door.newRoomSpawnLocation)
            break

        #Check Collision with Wall
        wallCollisionDictionary = pygame.sprite.groupcollide(playerGroup, self.wallGroup, False, False)
        if len(wallCollisionDictionary) > 0:
            return True
        
    def get_player(self):
        return self.player

