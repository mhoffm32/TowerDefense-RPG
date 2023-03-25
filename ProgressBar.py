import pygame
from ExplorationMode.Player import Player

# includes coins, level, diamonds, clock/timer


class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.diamond_count = 0
        self.coin_count = 0
        self.level = 0
        self.levelPoints = 0  # out of 100
        self.surface = surface
        self.seconds = 180
        self.timeRemaining = self.seconds
        self.clock = pygame.time.Clock()
        self.clockImg_index = 1
        self.messageRequest = False
        self.messageCount = 0
        self.paused = False

        self.timePaused = 0
        self.msgIndex = 0

        self.timeRunning = pygame.time.get_ticks()/1000

        self.font = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 28)
        self.attackMode = False

        #diamond_img = pygame.image.load('Images/Diamond.png')
        self.diamond_img = pygame.transform.scale(
            pygame.image.load('Images/Diamond.png'), (75, 75))
        self.coin_img = pygame.transform.scale(
            pygame.image.load('Images/Coin.png'), (75, 75))
        self.current_clock_img = pygame.transform.scale(
            pygame.image.load('Images/clock/clock1.png'), (40, 40))

        self.clock_images = [pygame.transform.scale(
            pygame.image.load('Images/clock/clock4.png'), (38, 38)), pygame.transform.scale(
            pygame.image.load('Images/clock/clock2.png'), (38, 38)), pygame.transform.scale(
            pygame.image.load('Images/clock/clock1.png'), (38, 38)), pygame.transform.scale(
            pygame.image.load('Images/clock/clock3.png'), (38, 38))]

        self.diamond_rect = self.diamond_img.get_rect()
        self.coin_rect = self.coin_img.get_rect()
        self.clock_rect = self.current_clock_img.get_rect()

        # width 1100 and height 90
        self.rect = pygame.Rect(0, 0, surface.get_width(), 90)

        rect_width = 550
        rect_height = 20
        self.levelProgress_rect = pygame.Rect((self.surface.get_width(
        ) - rect_width) // 2, (self.rect.height + rect_height)*2 // 3 - 15, rect_width, rect_height)

        # self.update()
        # asyncio.run(self.timer(120))
        pygame.display.update()

    def updateLevelProgress_Text(self):

        text = self.font.render("Level " + str(self.level), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.x = self.levelProgress_rect.x+self.levelProgress_rect.width+5
        textRect.y = self.levelProgress_rect.centery - textRect.height/2
        self.surface.blit(text, textRect)

        text = self.font.render(
            str("{:.0f}".format(self.levelPoints)) + " %", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.x = self.levelProgress_rect.x - textRect.width - 7
        textRect.y = self.levelProgress_rect.centery - textRect.height/2
        self.surface.blit(text, textRect)

    def add_xp(self, points=0):

        fillRect = self.levelProgress_rect.copy()
        fillRect.width = float(
            self.levelProgress_rect.width)*self.levelPoints/100

        self.levelPoints += points

        if self.levelPoints >= 100:
            self.level += 1
            self.levelPoints = 0
            self.setMessage(["level up"])
            fillRect.width = 0

        pygame.draw.rect(self.surface, (184, 24, 27),
                         fillRect)

    def reset_timer(self, seconds):
        self.seconds = seconds

    def add_coin(self, amount=1):
        self.coin_count += amount

    def add_diamond(self, amount=1):
        self.diamond_count += amount

    def setPlayer(self, name,gender,skin,hair,surface,pBar):
        self.player = Player(name,gender,skin,
                             hair,surface, pBar)
    

    def updateDiamondText(self):
        text = self.font.render(str(self.diamond_count), True, (0, 0, 0))
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
                           self.clock_images[self.clockImg_index].get_width() - 5, 25)
        self.surface.blit(text, textRect)

    def popUpMessage(self):
        self.paused = True  # texts is an array
        width = 500
        height = 300
        x = self.surface.get_width()/2 - width/2

        popUp_rect = pygame.Rect(x, 200, width, height)
        pygame.draw.rect(self.surface, (10, 74, 11), popUp_rect)
        pygame.draw.rect(self.surface, (255, 255, 255),
                         popUp_rect, width=2)
        text = self.font.render(
            str(self.texts[self.msgIndex]), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (popUp_rect.center)
        self.surface.blit(text, textRect)

    def setMessage(self, texts):
        self.messageRequest = True
        self.texts = texts
        self.messageCount = len(texts)

    def messageBoolean(self):
        if(self.messageRequest):
            if(self.msgIndex < (self.messageCount)):
                self.messageRequest = True
                return True
            else:
                self.msgIndex = 0
                self.messageCount = 0
                self.messageRequest = False
                self.paused = False
                return False
        else:
            return False

    def updateTime(self):
        elapsedTime = pygame.time.get_ticks()/1000
        if not self.paused:
            self.timeRemaining = self.seconds - elapsedTime + self.timePaused
            self.deltaT = self.seconds-self.timeRemaining
            self.prevTime = self.timeRemaining
        else:
            self.timePaused = elapsedTime - self.deltaT
            self.timeRemaining = self.prevTime

        if self.timeRemaining < 0:
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
        self.add_xp()
        self.updateLevelProgress_Text()
        pygame.draw.rect(self.surface, (0, 0, 0),
                         self.levelProgress_rect, width=2)

        self.surface.blit(self.diamond_img,
                          ((self.surface.get_width()/3), -10))

        self.surface.blit(self.coin_img, ((self.surface.get_width() -
                                           self.coin_img.get_width())/2, -10))

        curr_clkImg = self.clock_images[self.clockImg_index]

        self.surface.blit(curr_clkImg, (self.surface.get_width()
                          * 2/3 - curr_clkImg.get_width(), 5))

        self.updateDiamondText()
        self.updateCoinText()
        self.updateClockText()
