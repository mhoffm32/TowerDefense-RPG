import pygame


class Item():
    def __init__(self, price, type):
        self.price = price
        self.type = type
        #self.image = pygame.image.load(image_url)
        self.purchased = False
        self.equipped = False
        self.rect = pygame.Rect(0, 0, 1, 1)

        self.font = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 27)
        self.font2 = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 22)

        self.coin_img = pygame.image.load('Images/coin.png')

    def blitLabel(self, surface, x, y):

        text = self.font.render(
            str(self.price), True, (0, 0, 0))
        rect = text.get_rect()
        rect.center = (x, y)
        surface.blit(text, rect)
        surface.blit(
            pygame.transform.scale((self.coin_img), (35, 35)), (rect.x-30, rect.y))

        if not self.purchased:
            text = "Purchase"
            fill = (28, 105, 24)
        else:
            fill = (37, 65, 148)
            text = "Equipped"

        purchase_text = self.font.render(text, True,
                                         (255, 255, 255), fill)
        purchase_rect = purchase_text.get_rect()
        purchase_rect.center = (rect.centerx, rect.centery+40)

        bg_rect = pygame.Rect(0, 0, 90, 35)
        bg_rect.center = purchase_rect.center
        pygame.draw.rect(surface, fill,
                         bg_rect)

        surface.blit(purchase_text, purchase_rect)

        self.rect = bg_rect

    def getImage(self, surface):
        return


class Pet_item(Item):

    def __init__(self, price, image_url):
        super().__init__(price, 'pet')

        self.image = pygame.image.load(image_url)

        self.l_image = pygame.transform.scale(
            pygame.image.load(image_url), (35, 35))

        self.r_image = pygame.transform.scale(pygame.transform.flip(
            pygame.image.load(image_url), True, False), (35, 35))

    def blitLabel(self, surface, x, y):

        text = self.font.render(
            str(self.price), True, (0, 0, 0))
        rect = text.get_rect()
        rect.center = (x, y)
        surface.blit(text, rect)
        surface.blit(
            pygame.transform.scale((self.coin_img), (35, 35)), (rect.x-30, rect.y))

        if not self.purchased:
            text = "Purchase"
            fill = (28, 105, 24)
        else:
            fill = (37, 65, 148)
            if self.equipped:
                text = "Equipped"
            else:
                text = "Equip " + self.type

        purchase_text = self.font.render(text, True,
                                         (255, 255, 255), fill)
        purchase_rect = purchase_text.get_rect()
        purchase_rect.center = (rect.centerx, rect.centery+50)

        bg_rect = pygame.Rect(0, 0, 100, 35)
        bg_rect.center = purchase_rect.center

        pygame.draw.rect(surface, fill,
                         bg_rect)
        surface.blit(purchase_text, purchase_rect)

        self.rect = bg_rect


class TD_item(Item):

    def __init__(self, price, name, increase, stat):
        super().__init__(price, 'td upgrade')
        self.name = name
        self.stat = stat
        self.oldStat = stat
        self.increase = increase

    def blitLabel(self, surface, x, y):

        textSurf = self.font.render(
            str(self.price), True, (0, 0, 0))
        textrect = textSurf.get_rect()

        if not self.purchased:
            text = "Purchase"
            fill = (28, 105, 24)
        else:
            fill = (37, 65, 148)
            text = "Equipped"

        purchase_text = self.font.render(text, True,
                                         (255, 255, 255), fill)
        purchase_rect = purchase_text.get_rect()

        outer = pygame.Rect(x, y-50, 200, 25)

        innerW = (float(self.stat)/(self.oldStat+self.increase))*outer.width
        inner = pygame.Rect(x, outer.y, innerW, outer.height)
        outer.centerx = x
        inner.x = outer.x

        prevStat = pygame.font.SysFont('Times', 20).render(
            str(self.oldStat), True, (0, 0, 0))
        prevStatR = prevStat.get_rect()
        prevStatR.centery = outer.centery
        prevStatR.x = outer.x+5

        increaseStat = pygame.font.SysFont('Times', 20).render(
            "+"+str(self.increase), True, (0, 0, 0))
        increaseStatR = increaseStat.get_rect()
        increaseStatR.centery = outer.centery
        increaseStatR.right = outer.right - 5

        text1 = self.font2.render(self.name + "Increase", True, (0, 0, 0))
        rect1 = text1.get_rect()
        rect1.center = (x, y-75)

        textrect.center = (outer.right + 35, outer.centery)
        purchase_rect.center = (outer.centerx, textrect.centery+40)

        surface.blit(textSurf, textrect)
        surface.blit(
            pygame.transform.scale((self.coin_img), (37, 37)), (textrect.x - 30, textrect.y-5))

        bg_rect = pygame.Rect(0, 0, 100, 35)
        bg_rect.center = purchase_rect.center
        pygame.draw.rect(surface, fill, bg_rect)
        surface.blit(purchase_text, purchase_rect)

        pygame.draw.rect(surface, (51, 153, 255), outer)
        pygame.draw.rect(surface, (0, 89, 179), inner)
        pygame.draw.rect(surface, (0, 0, 0), outer, width=2)

        surface.blit(prevStat, prevStatR)
        surface.blit(increaseStat, increaseStatR)
        surface.blit(text1, rect1)

        self.rect = bg_rect
