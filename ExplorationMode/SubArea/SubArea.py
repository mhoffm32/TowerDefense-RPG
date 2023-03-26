from ExplorationMode.SubArea.Wall import Wall
from ExplorationMode.SubArea.Door import Door
from ExplorationMode.SubArea.Item import Item
from ExplorationMode.Player import Player
from ExplorationMode.SubArea.FriendlyCharacter import FriendlyCharacter

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
        self.screen = screen
        self.wallGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.itemGroup = pygame.sprite.Group()
        self.roomItemGroup = pygame.sprite.Group()
        self.npcGroup = pygame.sprite.Group()

        self.playerGroup = pygame.sprite.Group()
        self.player = Player(0,0,0,0,screen, self, progressBar)
        self.playerGroup.add(self.player)

        self.generateItems()
        self.generateRoom(roomNumber)


    def update(self):
        self.screen.blit(self.background, (0, 0))

        self.wallGroup.draw(self.screen)
        self.doorGroup.draw(self.screen)
        self.roomItemGroup.draw(self.screen)
        self.npcGroup.draw(self.screen)

        self.player.update()
        self.playerGroup.draw(self.screen)
        self.npcGroup.update()

    def generateRoom(self, roomNumber):
        self.roomNumber = roomNumber
        self.wallGroup.empty()
        self.doorGroup.empty()
        self.roomItemGroup.empty()
        self.npcGroup.empty()

        background_path = backgrounds.get(roomNumber, 'Images/backgrounds/brown_stone_floor.png')
        self.background = pygame.image.load(background_path)

        if roomNumber == 0:
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))


            npcText = ["Hello Player! welcome to the castle. However there is something you need to know. you know of the tree correct?", "Legend states that long ago there was the ability to destroy it. The power was stored within a powerful crystal however it", "was said to be destroyed many centuries ago. However I believe the fragments still exist and when put back together, will", "have the power to once again destroy the tree. Here, you can have my crystal fragment. I collected this a while ago.",  "Maybe you can recreate the crystal. Although I hope you never need to use it."]
            self.npcGroup.add(FriendlyCharacter(100,350, self.screen, npcText, self.player, 0, 1, 5))

            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 1, [500,500]))

            for item in self.itemGroup:
                if item.room == roomNumber:
                    self.roomItemGroup.add(item)

        elif roomNumber == 1:
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))

            self.wallGroup.add(Wall(800, 300, 1000,38, 'Images/mapObjects/walls/1000x38_wall.png'))
            self.wallGroup.add(Wall(200, 400, 500,38, 'Images/mapObjects/walls/1000x38_wall.png'))


            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 0, [500,200]))

            for item in self.itemGroup:
                if item.room == roomNumber:
                    self.roomItemGroup.add(item)
        elif roomNumber == 2:
            self.wallGroup.add(Wall(15,450,35,700, 'Images/mapObjects/walls/35x700_hedge_wall.png'))
            self.wallGroup.add(Wall(985,450,35,700, 'Images/mapObjects/walls/35x700_hedge_wall.png'))
            self.wallGroup.add(Wall(500,100,1000,38, 'Images/mapObjects/walls/1000x38_hedge_wall.png'))
            self.wallGroup.add(Wall(500, 685, 1000,38, 'Images/mapObjects/walls/1000x38_hedge_wall.png'))

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

            npcCollisionDictionary = pygame.sprite.groupcollide(self.npcGroup, self.playerGroup, False, False)
            for npc in npcCollisionDictionary:
                npc.interacting = True

        #Check Collision with Door

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


