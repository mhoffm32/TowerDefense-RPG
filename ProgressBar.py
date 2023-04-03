import pygame
import time
from ExplorationMode.Player import Player
from Item import Pet_item, TD_item

# includes coins, level, diamonds, clock/timer,
# link between updates in tower defense
# links store items and game
# keeps track of time for tower defense mode, and pause button


class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.diamond_count = 0
        self.coin_count = 100
        self.level = 0
        self.xp = 50  # out of 100
        self.surface = surface
        self.paused = False
        self.pet = None
        self.win = False
        self.lose = False

        self.progressFill = (75, 148, 49)

        # time stuff
        self.seconds = 180
        self.timeRemaining = self.seconds
        self.time1 = time.time()
        self.time2 = self.time1+self.seconds

        # message stuff
        self.messageRequest = False
        self.messageCount = 0
        self.msgIndex = 0

        self.td_items = {'archerDamage': TD_item(20, "Archer Damage", 40, 60),
                         'archerAttackSpeed': TD_item(30, "Archer Attack Speed", 1000, 2000),
                         'pikemanDamage': TD_item(30, "Pikeman Damage", 30, 90),
                         'pikemanAttackSpeed': TD_item(30, "Pikeman Attack Speed", 1000, 2000),
                         'ballistaAttackSpeed': TD_item(30, "Ballista Attack Speed", 2000, 5000),
                         'ballistaProjectileHealth': TD_item(30, "Ballista Projectile Health", 50, 120),
                         'towerHealth': TD_item(20, "Tower Health", 300, 700),
                         'cannonAttackSpeed': TD_item(20, "Cannon Attack Speed", 2000, 6000),
                         'cannonDamage': TD_item(20, "Cannon Damage", 100, 200),
                         'cannonRange': TD_item(20, "Cannon Range", 100, 200)}

        self.defenderStats = {}
        for k in self.td_items:
            self.defenderStats[k] = self.td_items[k].stat

        self.pet_items = {'red': Pet_item(60, 'Images/dragons/reddragon.png'),
                          'green': Pet_item(40, 'Images/dragons/greendragon.png'), 'purple': Pet_item(80, 'Images/dragons/purpledragon.png')}

        self.font = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 28)
        self.attackMode = False

        #diamond_img = pygame.image.load('Images/Diamond.png')
        self.diamond_img = pygame.transform.scale(
            pygame.image.load('Images/Diamond.png'), (75, 75))
        self.coin_img = pygame.transform.scale(
            pygame.image.load('Images/Coin.png'), (75, 75))

        self.clock_img = pygame.transform.scale(
            pygame.image.load('Images/clock/clock2.png'), (38, 38))

        self.diamond_rect = self.diamond_img.get_rect()
        self.coin_rect = self.coin_img.get_rect()
        self.clock_rect = self.clock_img.get_rect()

        # width 1100 and height 90
        self.rect = pygame.Rect(0, 0, surface.get_width(), 90)

        rect_width = 550
        rect_height = 20
        self.levelProgress_rect = pygame.Rect((self.surface.get_width(
        ) - rect_width) // 2, (self.rect.height + rect_height)*2 // 3 - 15, rect_width, rect_height)

        self.pause_msg = "pause"
        self.pause_text = self.font.render(self.pause_msg, True,
                                           (0, 0, 0), (3, 73, 171))
        self.pause_rect = self.pause_text.get_rect()
        self.pause_rect.center = (40, 25)
        self.bg_rect = pygame.Rect(0, 0, 60, 35)
        self.bg_rect.center = self.pause_rect.center
        pygame.draw.rect(self.surface, (3, 73, 171),
                         self.bg_rect)
        self.surface.blit(self.pause_text, self.pause_rect)
        pygame.display.update()

    def purchase_td_upgrade(self, key):
        item = self.td_items[key]
        if not item.purchased:
            if(item.price <= self.coin_count):
                item.purchased = True
                item.equipped = True
                item.stat += item.increase
                self.coin_count -= item.price
                self.defenderStats[key] = item.stat
            else:
                self.setMessage(["You don't have enough coins!"])

    def purchase_pet_item(self, key):
        item = self.pet_items[key]
        if(item.price <= self.coin_count):
            item.purchased = True
            self.coin_count -= item.price
        else:
            self.setMessage(["You don't have enough coins!"])

    def equip_pet_item(self, key):
        # to buy a pet in the store and link it to the player sprite

        item = self.pet_items[key]

        if item.equipped:
            for k in self.pet_items:
                self.pet_items[k].equipped = False
                self.pet = None
        else:
            for k in self.pet_items:
                self.pet_items[k].equipped = False
            item.equipped = True
            self.pet = item

    def checkPause(self, events):
        # checking pause button clicked
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.bg_rect.collidepoint(event.pos):
                    if self.paused:
                        self.paused = False
                        self.pause_msg = "pause"
                        self.reset_timer(self.timeRemaining)
                    else:
                        self.pause_msg = "unpause"
                        self.paused = True

    def updateLevelProgress_Text(self):
        text = self.font.render("Progress", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.x = self.levelProgress_rect.x+self.levelProgress_rect.width+5
        textRect.y = self.levelProgress_rect.centery - textRect.height/2
        self.surface.blit(text, textRect)

        text = self.font.render(
            str("{:.0f}".format(self.xp)) + " %", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.x = self.levelProgress_rect.x - textRect.width - 7
        textRect.y = self.levelProgress_rect.centery - textRect.height/2
        self.surface.blit(text, textRect)

    def update_xp(self, points=0):
        # updates xp bar when points are added or lost

        fillRect = self.levelProgress_rect.copy()
        fillRect.width = float(
            self.levelProgress_rect.width)*self.xp/100

        self.xp += points

        pygame.draw.rect(self.surface, self.progressFill,
                         fillRect)

        if self.xp >= 100:
            time.sleep(0.5)
            self.win = True
        elif self.xp <= 0:
            time.sleep(0.5)
            self.lose = True

        pygame.draw.rect(self.surface, self.progressFill,
                         fillRect)

    def reset_timer(self, seconds):
        # for after attack mode and after pausing
        self.seconds = seconds
        self.time1 = time.time()
        self.time2 = self.time1+self.seconds

    def add_coin(self, amount=1):
        self.coin_count += amount

    def add_diamond(self, amount=1):
        self.diamond_count += amount

    def setPlayer(self, name, gender, skin, hair, surface, pBar):
        self.player = Player(name, gender, skin,
                             hair, surface, pBar)

    def updateDiamondText(self):
        text = self.font.render(
            str(self.diamond_count) + "/6", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.surface.get_width()/3 +
                           self.diamond_img.get_width()-3, 25)
        self.surface.blit(text, textRect)

    def updateCoinText(self):
        text = self.font.render(str(self.coin_count), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = ((self.surface.get_width() +
                            self.coin_img.get_width())/2 - 3, 25)
        self.surface.blit(text, textRect)

    def updateClockText(self):
        minutes = "{:.0f}".format(self.timeRemaining // 60)
        seconds = "{:.0f}".format(self.timeRemaining % 60)

        text = self.font.render(
            str("{}:{}".format(minutes, seconds)), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.surface.get_width()*2/3 +
                           self.clock_img.get_width() - 5, 25)
        self.surface.blit(text, textRect)

    def popUpMessage(self):
        # self.paused = True  # texts is an array
        width = 500
        height = 150
        x = self.surface.get_width()/2 - width/2

        popUp_rect = pygame.Rect(x, 300, width, height)
        pygame.draw.rect(self.surface, (10, 74, 11), popUp_rect)
        pygame.draw.rect(self.surface, (255, 255, 255),
                         popUp_rect, width=2)

        text = self.font.render(
            str(self.texts[self.msgIndex]), True, (255, 255, 255))
        text2 = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 18).render(
            'space bar to continue', True, (255, 255, 255))
        text2Rect = text2.get_rect()
        text2Rect.center = (popUp_rect.centerx, 430)
        textRect = text.get_rect()
        textRect.center = (popUp_rect.center)
        self.surface.blit(text, textRect)
        self.surface.blit(text2, text2Rect)

    def setMessage(self, texts):
        self.messageRequest = True
        self.texts = texts
        self.messageCount = len(texts)

    def set_player(self, player):
        self.player = player

    def messageBoolean(self):
        if(self.messageRequest):
            if(self.msgIndex < (self.messageCount)):
                self.messageRequest = True
                return True
            else:
                self.msgIndex = 0
                self.messageCount = 0
                self.messageRequest = False
                #self.paused = False
                return False
        else:
            return False

    def updateTime(self):

        if self.paused:
            self.timeRemaining = self.time_copy
        else:
            self.timeRemaining = self.time2-time.time()
            self.time_copy = self.timeRemaining

        if self.timeRemaining <= 0:
            self.attackMode = True

    def update(self, events):

        if(self.messageBoolean()):
            self.popUpMessage()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.popUpMessage()
                        self.msgIndex += 1

        self.updateTime()

        pygame.draw.rect(self.surface, pygame.Color((138, 103, 76)), self.rect)
        pygame.draw.rect(self.surface, pygame.Color(
            (0, 0, 0)), self.rect, width=2)

        pygame.draw.rect(self.surface, (247, 228, 210),
                         self.levelProgress_rect)
        self.update_xp()
        self.updateLevelProgress_Text()
        pygame.draw.rect(self.surface, (0, 0, 0),
                         self.levelProgress_rect, width=2)

        self.surface.blit(self.diamond_img,
                          ((self.surface.get_width()/3), -10))

        self.surface.blit(self.coin_img, ((self.surface.get_width() -
                                           self.coin_img.get_width())/2, -10))

        self.surface.blit(self.clock_img, (self.surface.get_width()
                          * 2/3 - self.clock_img.get_width(), 5))

        # pause thing
        self.pause_text = self.font.render(self.pause_msg, True,
                                           (0, 0, 0), (3, 73, 171))
        self.pause_rect = self.pause_text.get_rect()
        self.pause_rect.center = (45, 25)
        self.bg_rect = pygame.Rect(0, 0, 70, 35)
        self.bg_rect.center = self.pause_rect.center
        pygame.draw.rect(self.surface, (3, 73, 171),
                         self.bg_rect)
        self.surface.blit(self.pause_text, self.pause_rect)
        pygame.draw.rect(self.surface, (0, 0, 0),
                         self.bg_rect, width=2)

        self.checkPause(events)
        self.updateDiamondText()
        self.updateCoinText()
        self.updateClockText()
