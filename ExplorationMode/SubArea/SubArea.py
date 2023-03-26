from ExplorationMode.SubArea.Wall import Wall
from ExplorationMode.SubArea.Door import Door
from ExplorationMode.SubArea.Item import Item
from ExplorationMode.Player import Player
from ExplorationMode.SubArea.FriendlyCharacter import FriendlyCharacter

import pygame

backgrounds = {
    0: 'Images/backgrounds/brown_stone_floor.png',
    1: 'Images/backgrounds/wood_floor.png',
    3: 'Images/backgrounds/wood_floorV2.png',
    4: 'Images/backgrounds/wood_floorV2.png',
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
        self.roomNPCGroup = pygame.sprite.Group()

        self.playerGroup = pygame.sprite.Group()
        self.player = Player(screen, progressBar, 50, 70, self)
        self.playerGroup.add(self.player)

        self.generateItems()
        self.generateNPCs()
        self.generateRoom(roomNumber)


    def update(self):
        self.screen.blit(self.background, (0, 0))

        self.wallGroup.draw(self.screen)
        self.doorGroup.draw(self.screen)
        self.roomItemGroup.draw(self.screen)
        self.roomNPCGroup.draw(self.screen)

        self.player.update()
        self.playerGroup.draw(self.screen)
        self.npcGroup.update()

    def generateRoom(self, roomNumber):
        self.roomNumber = roomNumber
        self.wallGroup.empty()
        self.doorGroup.empty()
        self.roomItemGroup.empty()
        self.roomNPCGroup.empty()

        background_path = backgrounds.get(roomNumber, 'Images/backgrounds/brown_stone_floor.png')
        self.background = pygame.image.load(background_path)

        if roomNumber == 0: #the courtyard
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 1, [500,500]))
            self.doorGroup.add(Door(-10,350,'Images/mapObjects/door_side_sprite.png', 6, [820,350]))
            self.doorGroup.add(Door(910,350,'Images/mapObjects/door_side_sprite.png', 7, [140,350]))


        elif roomNumber == 6: #the shop
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))



            self.doorGroup.add(Door(910,350,'Images/mapObjects/door_side_sprite.png', 0, [140,350]))            


        elif roomNumber == 7: #the immortal tree
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))


            self.doorGroup.add(Door(-10,350,'Images/mapObjects/door_side_sprite.png', 0, [820,350]))


        elif roomNumber == 1: #maybe add stairs as an obstacle and the entry to the castle
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            self.wallGroup.add(Wall(800, 300, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(200, 400, 500,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))


            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 0, [500,200]))
            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 2, [500,500]))


        elif roomNumber == 2: #castle entrance 
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            


            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 1, [500,200]))
            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 3, [500,500]))
            


        elif roomNumber == 3: #throne room
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))



            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 2, [500,200]))
            self.doorGroup.add(Door(350,85,'Images/mapObjects/door_sprite.png', 4, [500,500]))
            self.doorGroup.add(Door(-10,350,'Images/mapObjects/door_side_sprite.png', 5, [820,350]))


        elif roomNumber == 4: #king/queen's quarters for customization
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))



            self.doorGroup.add(Door(350,660,'Images/mapObjects/door_sprite.png', 3, [500,200]))
              


        elif roomNumber == 5: #castle library
            self.wallGroup.add(Wall(0,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965,0,35,700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0,87,1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000,38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))



            self.doorGroup.add(Door(910,350,'Images/mapObjects/door_side_sprite.png', 3, [140,350]))

        for item in self.itemGroup:
            if item.room == roomNumber:
                self.roomItemGroup.add(item)

        for npc in self.npcGroup:
            if npc.room == roomNumber:
                self.roomNPCGroup.add(npc)

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

    def generateNPCs(self):
        npcText = ["Hello Player! Welcome to the castle. There is something you need to know! You know of The Tree correct?", "Legend states that long ago there was the ability to destroy it. The power was stored within a powerful crystal that", "was said to be destroyed many centuries ago. However I believe the fragments still exist and when put back together, will", "have the power to once again destroy The Tree! Here, you can have my crystal fragment. I collected this a while ago.",  "Maybe you can recreate the crystal. Although I hope you never need to use it."]
        self.npcGroup.add(FriendlyCharacter(100,550, self.screen, npcText, self.player, 0, 1, 5, 0))



