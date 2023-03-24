from ExplorationMode.SubArea.Wall import Wall
from ExplorationMode.SubArea.Door import Door
from ExplorationMode.SubArea.Item import Item
from ExplorationMode.Player import Player

import pygame

backgrounds = {
    0: 'Images/backgrounds/brown_stone_floor.png',
    1: 'Images/backgrounds/wood_floor.png',
    # more room backgrounds here
}

class SubArea:
    def __init__(self, roomNumber, screen, progressBar, background):
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
        self.screen.blit(self.background, (0, 0))

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

        background_path = backgrounds.get(roomNumber, 'Images/backgrounds/brown_stone_floor.png')
        self.background = pygame.image.load(background_path)

        if roomNumber == 0: #the courtyard
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))

            

            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 1, [500,500]))
            self.doorGroup.add(Door(-10,350,'Images/mapObjects/door_side_sprite.png', 6, [820,350]))
            self.doorGroup.add(Door(910,350,'Images/mapObjects/door_side_sprite.png', 7, [140,350]))

            for item in self.itemGroup:
                if item.room == roomNumber:
                    self.roomItemGroup.add(item)


        elif roomNumber == 6: #the shop
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))



            self.doorGroup.add(Door(910,350,'Images/mapObjects/door_side_sprite.png', 0, [140,350]))            


        elif roomNumber == 7: #the immortal tree
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))


            self.doorGroup.add(Door(-10,350,'Images/mapObjects/door_side_sprite.png', 0, [820,350]))


        elif roomNumber == 1: #maybe add stairs as an obstacle and the entry to the castle
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))

            self.wallGroup.add(Wall(800, 300, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(200, 400, 500,38, 'Images/mapObjects/walls/1000x38_wall.png'))


            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 0, [500,200]))
            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 2, [500,500]))

            for item in self.itemGroup:
                if item.room == roomNumber:
                    self.roomItemGroup.add(item)


        elif roomNumber == 2: #castle entrance 
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            


            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 1, [500,200]))
            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 3, [500,500]))
            


        elif roomNumber == 3: #throne room
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))



            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 2, [500,200]))
            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 4, [500,500]))
            self.doorGroup.add(Door(-10,350,'Images/mapObjects/door_side_sprite.png', 5, [820,350]))


        elif roomNumber == 4: #king/queen's quarters for customization
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))



            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 3, [500,200]))
              


        elif roomNumber == 5: #castle library
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))



            self.doorGroup.add(Door(910,350,'Images/mapObjects/door_side_sprite.png', 3, [140,350]))

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
        if(keysPressed[pygame.K_f]):
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


