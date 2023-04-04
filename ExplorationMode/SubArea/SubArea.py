from ExplorationMode.SubArea.Wall import Wall
from ExplorationMode.SubArea.Door import Door
from ExplorationMode.SubArea.Item import Item
from ExplorationMode.SubArea.Furniture import Furniture
from ExplorationMode.SubArea.FriendlyCharacter import FriendlyCharacter, ShopKeeper
import pygame

# background dictionary to store backgrounds depending on the room
backgrounds = {
    0: 'Images/backgrounds/courtyard.png',
    1: 'Images/backgrounds/entrance1.png',
    2: 'Images/backgrounds/hallway.png',
    3: 'Images/backgrounds/throne_room_floor.png',
    4: 'Images/backgrounds/wood_floorV2.png',
    5: 'Images/backgrounds/wood_floorV2.png',
    6: 'Images/backgrounds/wood_floor.png',
    7: 'Images/backgrounds/garden.png'
}

# controls the entirety of exploration mode
class SubArea:
    def __init__(self, roomNumber, screen, progressBar, player):
        print("Initialize Sub Area")
        self.roomNumber = roomNumber
        self.screen = screen
        self.progressBar = progressBar
        self.wallGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.itemGroup = pygame.sprite.Group()
        self.roomItemGroup = pygame.sprite.Group()
        self.npcGroup = pygame.sprite.Group()
        self.roomNPCGroup = pygame.sprite.Group()
        self.furnitureGroup = pygame.sprite.Group()

        self.playerGroup = pygame.sprite.Group()
        self.player = player
        self.player.setRoom(self)
        self.playerGroup.add(self.player)

        self.generateItems()
        self.generateNPCs()
        self.generateRoom(roomNumber)

    def update(self):
        self.screen.blit(self.background, (0, 0))

        self.checkCollision()

        self.wallGroup.draw(self.screen)
        self.doorGroup.draw(self.screen)
        self.roomItemGroup.draw(self.screen)
        self.roomNPCGroup.draw(self.screen)
        self.furnitureGroup.draw(self.screen)
        self.player.update()
        self.playerGroup.draw(self.screen)
        self.roomNPCGroup.update()

    def generateRoom(self, roomNumber):
        self.roomNumber = roomNumber
        self.wallGroup.empty()
        self.doorGroup.empty()
        self.roomItemGroup.empty()
        self.roomNPCGroup.empty()
        self.furnitureGroup.empty()

        background_path = backgrounds.get(roomNumber, 'Images/backgrounds/brown_stone_floor.png')
        self.background = pygame.image.load(background_path)

        if roomNumber == 0:  # the courtyard
            # border walls
            self.wallGroup.add(Wall(0, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965, 0, 35, 700, 'Images/mapObjects/walls/35x700_hedge_wall.png'))
            self.wallGroup.add(Wall(0, 87, 1000, 38, 'Images/mapObjects/walls/1000x38_hedge_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000, 38, 'Images/mapObjects/walls/1000x38_hedge_wall.png'))

            # doors
            self.doorGroup.add(Door(440, 85, 'Images/mapObjects/door_sprite.png', 1, [500, 500]))
            self.doorGroup.add(Door(-10, 330, 'Images/mapObjects/door_side_sprite.png', 6, [820, 350]))
            self.doorGroup.add(Door(910, 420, 'Images/mapObjects/door_side_sprite.png', 7, [140, 350]))

            # furniture obstacles
            self.furnitureGroup.add(Furniture(20, 140, 70, 130, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(890, 140, 70, 130, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(40, 400, 70, 60, 'Images/mapObjects/shop_sign.png'))

        elif roomNumber == 1: # entrance to castle
            # border walls
            self.wallGroup.add(Wall(215, 440, 565, 30, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(-720, 235, 1000, 30, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(720, 235, 1000, 30, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            # inner walls to create staircase effect
            self.wallGroup.add(Wall(0, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0, 87, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            # doors
            self.doorGroup.add(Door(350, 660, 'Images/mapObjects/door_sprite.png', 0, [500, 200]))
            self.doorGroup.add(Door(440, 85, 'Images/mapObjects/door_sprite.png', 2, [500, 500]))

        elif roomNumber == 2:  # hallway leading to throne room
            # border walls
            self.wallGroup.add(Wall(350, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(640, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0, 87, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            # doors
            self.doorGroup.add(Door(440, 660, 'Images/mapObjects/door_sprite.png', 1, [500, 200]))
            self.doorGroup.add(Door(440, 85, 'Images/mapObjects/door_sprite.png', 3, [500, 500]))

            # furniture obstacles
            self.furnitureGroup.add(Furniture(370, 100, 70, 130, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(370, 300, 70, 130, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(370, 500, 70, 130, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(590, 100, 70, 130, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(590, 300, 70, 130, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(590, 500, 70, 130, 'Images/mapObjects/plant3.png'))

        elif roomNumber == 3:  # throne room
            # border walls
            self.wallGroup.add(Wall(0, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0, 87, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            # doors
            self.doorGroup.add(Door(440, 660, 'Images/mapObjects/door_sprite.png', 2, [500, 200]))
            self.doorGroup.add(Door(440, 85, 'Images/mapObjects/door_sprite.png', 4, [500, 500]))
            self.doorGroup.add(Door(-10, 350, 'Images/mapObjects/door_side_sprite.png', 5, [820, 350]))

            # furniture obstacles
            self.furnitureGroup.add(Furniture(70, 120, 70, 110, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(860, 120, 70, 110, 'Images/mapObjects/plant4.png'))
            self.furnitureGroup.add(Furniture(860, 240, 70, 110, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(860, 360, 70, 110, 'Images/mapObjects/plant4.png'))
            self.furnitureGroup.add(Furniture(860, 480, 70, 110, 'Images/mapObjects/plant3.png'))
            self.furnitureGroup.add(Furniture(40, 260, 70, 60, 'Images/mapObjects/lib_sign.png'))
            self.furnitureGroup.add(Furniture(680, 70, 180, 190, 'Images/mapObjects/throne.png'))

        elif roomNumber == 4:  # king/queen's quarters for customization
            # border walls
            self.wallGroup.add(Wall(0, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0, 87, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            # door
            self.doorGroup.add(Door(440, 660, 'Images/mapObjects/door_sprite.png', 3, [500, 200]))

            # furniture obstacles
            self.furnitureGroup.add(Furniture(400, 100, 200, 200, 'Images/mapObjects/bed_sprite.png'))
            self.furnitureGroup.add(Furniture(330, 87, 70, 100, 'Images/mapObjects/dresser_sprite.png'))
            self.furnitureGroup.add(Furniture(600, 87, 70, 100, 'Images/mapObjects/dresser_sprite.png'))
            self.furnitureGroup.add(Furniture(70, 87, 70, 130, 'Images/mapObjects/plant1.png'))
            self.furnitureGroup.add(Furniture(900, 87, 70, 130, 'Images/mapObjects/plant1.png'))

        elif roomNumber == 5:  # castle library
            # border walls
            self.wallGroup.add(Wall(0, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0, 87, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            # door
            self.doorGroup.add(Door(910, 350, 'Images/mapObjects/door_side_sprite.png', 3, [140, 350]))

            # furniture obstacles
            self.furnitureGroup.add(Furniture(30, 100, 150, 160, 'Images/mapObjects/bookshelf_sprite.png'))
            self.furnitureGroup.add(Furniture(180, 100, 150, 160, 'Images/mapObjects/bookshelf_sprite.png'))
            self.furnitureGroup.add(Furniture(330, 100, 150, 160, 'Images/mapObjects/bookshelf_sprite.png'))
            self.furnitureGroup.add(Furniture(480, 100, 150, 160, 'Images/mapObjects/bookshelf_sprite.png'))
            self.furnitureGroup.add(Furniture(630, 100, 150, 160, 'Images/mapObjects/bookshelf_sprite.png'))
            self.furnitureGroup.add(Furniture(780, 100, 150, 160, 'Images/mapObjects/bookshelf_sprite.png'))
            self.furnitureGroup.add(Furniture(150, 360, 150, 160, 'Images/mapObjects/table_and_chair_sprite.png'))
            self.furnitureGroup.add(Furniture(350, 360, 150, 160, 'Images/mapObjects/table_and_chair_sprite.png'))
            self.furnitureGroup.add(Furniture(550, 360, 150, 160, 'Images/mapObjects/table_and_chair_sprite.png'))
            self.furnitureGroup.add(Furniture(900, 170, 70, 130, 'Images/mapObjects/lamp.png'))
            
        elif roomNumber == 6:  # the shop
            # border walls
            self.wallGroup.add(Wall(0, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(965, 0, 35, 700, 'Images/mapObjects/walls/35x700_stone_wall.png'))
            self.wallGroup.add(Wall(0, 87, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000, 38, 'Images/mapObjects/walls/1000x38_stone_wall.png'))

            # door
            self.doorGroup.add(Door(910, 350, 'Images/mapObjects/door_side_sprite.png', 0, [140, 350]))

            # furniture obstacles
            self.furnitureGroup.add(Furniture(500, 100, 200, 200, 'Images/mapObjects/empty_shelf.png'))
            self.furnitureGroup.add(Furniture(700, 100, 200, 200, 'Images/mapObjects/empty_shelf.png'))
            self.furnitureGroup.add(Furniture(150, 200, 200, 200, 'Images/mapObjects/shopkeeper_desk.png'))

        elif roomNumber == 7:  # the immortal tree
            # border walls
            self.wallGroup.add(Wall(0, 0, 35, 700, 'Images/mapObjects/walls/35x700_hedge_wall.png'))
            self.wallGroup.add(Wall(965, 0, 35, 700, 'Images/mapObjects/walls/35x700_hedge_wall.png'))
            self.wallGroup.add(Wall(0, 87, 1000, 38, 'Images/mapObjects/walls/1000x38_hedge_wall.png'))
            self.wallGroup.add(Wall(0, 662, 1000, 38, 'Images/mapObjects/walls/1000x38_hedge_wall.png'))

            # door
            self.doorGroup.add(Door(-10, 350, 'Images/mapObjects/door_side_sprite.png', 0, [820, 350]))

            # furniture obstacle
            self.furnitureGroup.add(Furniture(380, 200, 250, 290, 'Images/mapObjects/tree.png'))

        # adding items if they exist
        for item in self.itemGroup:
            if item.room == roomNumber:
                self.roomItemGroup.add(item)

        # adding npcs if they exist
        for npc in self.npcGroup:
            if npc.room == roomNumber:
                self.roomNPCGroup.add(npc)

    # method to check collision between player object and other objects
    def checkCollision(self):
        # Check Collision with Item
        keysPressed = pygame.key.get_pressed()
        # interact key in game is 'f'
        if(keysPressed[pygame.K_f]):
            itemCollisionDictionary = pygame.sprite.groupcollide(
                self.itemGroup, self.playerGroup, False, False)
            for item in itemCollisionDictionary:
                if item.room == self.roomNumber:
                    self.player.collectItem(item)
                    self.itemGroup.remove(item)
                    self.roomItemGroup.remove(item)

            # Check Collision with Door
            doorCollisionDictionary = pygame.sprite.groupcollide(
                self.doorGroup, self.playerGroup, False, False)

            for door in doorCollisionDictionary:
                self.generateRoom(door.nextLevelNumber)
                self.player.setPosition(door.newRoomSpawnLocation)
                break
            # npc collisions
            npcCollisionDictionary = pygame.sprite.groupcollide(
                self.npcGroup, self.playerGroup, False, False)
            for npc in npcCollisionDictionary:
                npc.interacting = True

        # Check Collision with Wall
        wallCollisionDictionary = pygame.sprite.groupcollide(
            self.playerGroup, self.wallGroup, False, False)
        if len(wallCollisionDictionary) > 0:
            return True

        # Check Collision with Furniture
        furnitureCollisionDictionary = pygame.sprite.groupcollide(
            self.playerGroup, self.furnitureGroup, False, False)
        if len(furnitureCollisionDictionary) > 0:
            return True

    def get_player(self):
        return self.player

    def generateItems(self):
        coin = 'Images/coin.png'
        crystal = 'Images/Diamond.png'

        # populating rooms with secret coins
        self.itemGroup.add(Item(50, 0, 0, 900, 600, 0, coin))
        self.itemGroup.add(Item(50, 0, 0, 900, 150, 1, coin))
        self.itemGroup.add(Item(50,0,0,100,150,3,coin))
        self.itemGroup.add(Item(50, 0, 0, 200, 150, 4, coin))
        self.itemGroup.add(Item(50, 0, 0, 40, 600, 5, coin))

        # populating rooms with secret crystal fragments
        self.itemGroup.add(Item(0, 1, 0, 100, 180, 1, crystal))
        self.itemGroup.add(Item(0,1,0,500,350,2,crystal))
        self.itemGroup.add(Item(0,1,0,900,600,3,crystal))
        self.itemGroup.add(Item(0, 1, 0, 800, 150, 4, crystal))
        self.itemGroup.add(Item(0, 1, 0, 40, 300, 5, crystal))
        self.itemGroup.add(Item(0,1,0,900,600,7,crystal))
        self.itemGroup.add(Item(0,1,0,500,440,7,crystal))

    def generateNPCs(self):
        # messenger npc in main area
        npcText = ["Hello your Majesty! I am the castle's new messenger. I must tell you something. You know of The Tree of Immortality, ", " correct? Legend states that long ago there was the ability to destroy it. The power was stored within a powerful crystal that",
                   "was said to be shattered many centuries ago. However I believe the fragments still exist and when put back together, will", " once again have the power to destroy The Tree! Here, you can have my crystal fragment. I found it a while ago.",  "Maybe you can rebuild the crystal. It may finally bring peace to this world. Although I hope you never need to use it."]
        self.npcGroup.add(FriendlyCharacter(100, 550, self.screen, npcText, self.player, 0, 1, 0, 0, 'Images/npc/npc1.png'))

        # shopkeeper npc
        shopkeeperText = ["Hello your Highness. Please purchase an upgrade for the tower defense here in this shop!",
                          "Also, I found this crystal on the ground. You can have it! Thanks for visiting."]
        shopKeeper = ShopKeeper(350, 150, self.screen, shopkeeperText,self.player, 0, 1, 0, 6, 'Images/npc/shopkeeper.png', self.progressBar)
        self.npcGroup.add(shopKeeper)

        # random guards
        defaultGuardText = ["Hope you are staying out of trouble your Highness.",
                            "Please be careful out there your Majesty, these are dangerous times.", "Hello. I hope you are doing well your Highness."]
        self.npcGroup.add(FriendlyCharacter(340, 120, self.screen, [defaultGuardText[0]], self.player, 0, 0, 0, 0, 'Images/npc/castle_guard1.png'))
        self.npcGroup.add(FriendlyCharacter(590, 120, self.screen, [defaultGuardText[2]], self.player, 0, 0, 0, 0, 'Images/npc/castle_guard2.png'))

        # castle entrance guards
        entranceGuardText = ["Welcome back to the castle your Highness.","Please come in your Majesty! It is not safe outside the castle."]
        self.npcGroup.add(FriendlyCharacter(340, 120, self.screen, [entranceGuardText[1]], self.player, 0, 0, 0, 1, 'Images/npc/castle_guard3.png'))
        self.npcGroup.add(FriendlyCharacter(590, 120, self.screen, [entranceGuardText[0]], self.player, 0, 0, 0, 1, 'Images/npc/castle_guard1.png'))

        # bedroom door guards
        bedroomGuardText = ["Past these doors are your bedroom chambers, your Highness.", "Welcome back your Highness."]
        self.npcGroup.add(FriendlyCharacter(340, 120, self.screen, [bedroomGuardText[0]], self.player, 0, 0, 0, 3, 'Images/npc/castle_guard2.png'))
        self.npcGroup.add(FriendlyCharacter(590, 120, self.screen, [bedroomGuardText[1]], self.player, 0, 0, 0, 3, 'Images/npc/castle_guard3.png'))

        # librarian guard
        libraryGuardText = ["Welcome to the Library, your Majesty. Feel free to look around."]
        self.npcGroup.add(FriendlyCharacter(700, 400, self.screen, libraryGuardText, self.player, 0, 0, 0, 5, 'Images/npc/castle_guard1.png'))

        # Tree Guard
        treeGuardText = ["Hello your Majesty. Isn't The Tree of Immortality just beautiful?","We must protect it at all costs.","Watch out for the Witch just past The Tree. She is untrustworthy."]
        self.npcGroup.add(FriendlyCharacter(300,400,self.screen,treeGuardText,self.player,0,0,0,7,'Images/npc/castle_guard2.png'))

        # Witch
        witchText = ["Hi there...","Legend has it, if you have 8 crystal fragments and you interact with The Tree, something may occur...","Ignore that guard over there. I promise I have no ill intentions!"]
        self.npcGroup.add(FriendlyCharacter(900,150,self.screen,witchText,self.player,0,0,0,7,"Images/npc/witch.png"))