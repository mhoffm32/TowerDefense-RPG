import pygame
from Character import Character
from ExplorationMode.SubArea.Item import Item
from ShopMenu import ShopMenu

pygame.init()

class FriendlyCharacter(Character):
    def __init__(self, x, y, screen, text, player, moneyValue, crystalValue, xpValue, room, img_path):
        super().__init__(x, y, img_path)
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.interactedWith = False
        self.interacting = False
        self.screen = screen
        self.textList = text
        self.player = player
        self.moneyValue = moneyValue
        self.crystalValue = crystalValue
        self.xpValue = xpValue
        self.room = room

    def update(self):
        if self.interacting:
            self.talk()

    def talk(self):
        rectHeight = ((len(self.textList)+1)*20) + 50
        rectY = 660 - rectHeight

        pygame.draw.rect(self.screen, (245, 198, 71),
                         pygame.Rect(60, rectY, 880, rectHeight))
        self.font = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 28)

        i = 0
        for text in self.textList:
            screenText = self.font.render(text, True, (0, 0, 0))
            textRect = screenText.get_rect()
            textRect.x = 80
            textRect.y = (i*25) + rectY + 10
            self.screen.blit(screenText, textRect)
            i += 1

        screenText = self.font.render("Press ESC to Close", True, (0, 0, 0))
        textRect = screenText.get_rect()
        textRect.x = 780
        textRect.y = 625
        self.screen.blit(screenText, textRect)

        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_ESCAPE]:
            self.interacting = False
            if not self.interactedWith:
                self.interactedWith = True
                self.player.collectItem(Item(
                    self.moneyValue, self.crystalValue, self.xpValue, 0, 0, 0, 'Images/coin.png'))


class ShopKeeper(FriendlyCharacter):
    def __init__(self, x, y, screen, text, player, moneyValue, crystalValue, xpValue, room, img_path,progressBar):
        super().__init__(x, y, screen, text, player,
                         moneyValue, crystalValue, xpValue, room, img_path)
        self.progressBar = progressBar

    def talk(self):
        super().talk()
        # button to enter store
        store_text = self.font.render("Enter Store", True,
                                      (255, 255, 255), (102, 39, 24))
        store_rect = store_text.get_rect()
        store_rect.center = (845, 588)
        self.storebg_rect = pygame.Rect(0, 0, 105, 45)
        self.storebg_rect.center = store_rect.center
        pygame.draw.rect(self.screen, (102, 39, 24),
                         self.storebg_rect)
        self.screen.blit(store_text, store_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.storebg_rect.collidepoint(event.pos):
                    ShopMenu(self.progressBar).mainMenu()
            if event.type == pygame.QUIT:
                pygame.quit()