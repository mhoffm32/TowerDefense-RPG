import pygame
import time
from ProgressBar import ProgressBar

pygame.init()


class ShopMenu():
    def __init__(self):

        self.main_screen = pygame.display.set_mode((1100, 800))
        self.pBar = ProgressBar(self.main_screen)

        self.main = True

        self.curr_screen = 'main'

        self.pet_items = self.pBar.pet_items
        self.td_items = self.pBar.td_items

        self.pBar_g = pygame.sprite.Group([self.pBar])

        self.font1 = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 38)

        self.titleFont = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 45)

        self.font2 = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 20)

        self.green_dragon = pygame.image.load(
            'Images/dragons/greendragon.png')
        self.purple_dragon = pygame.image.load(
            'Images/dragons/purpledragon.png')
        self.red_dragon = pygame.image.load('Images/dragons/reddragon.png')

        self.bow_img = pygame.image.load('Images/weapons/bow_arrow_sprite.png')

        self.coin_img = pygame.image.load('Images/coin.png')

        self.cannon_img = pygame.image.load(
            'Images/weapons/cannons_sprite_left.png')
        self.ballista_img = pygame.image.load(
            'Images/weapons/balista_sprite_left.png')
        self.pikeman_img = pygame.image.load(
            'Images/weapons/pikeman_left_idle_sprite.png')
        self.tower_img = pygame.image.load('Images/towerDefense/td_castle.png')
        # need archer image

    def mainMenu(self):
        screenRectangle = self.main_screen.get_rect()

        bg_color = (101, 150, 144)
        self.main_screen.fill(bg_color)

        # main screen stuff

        store_text = self.titleFont.render(
            "Shop", True, (0, 0, 0))
        store_rect = store_text.get_rect()
        store_rect.center = (screenRectangle.centerx, 100)

        weapon_upgrades = pygame.Rect(150, 270, 200, 200)
        td_upgrades = pygame.Rect(450, 270, 200, 200)
        pets = pygame.Rect(750, 270, 200, 200)

        weapon_text = self.font1.render(
            'Tower Defense Weapons', True, (0, 0, 0))
        weapon_rect = weapon_text.get_rect()
        weapon_rect.center = (weapon_upgrades.centerx,
                              weapon_upgrades.bottom+25)

        td_text = self.font1.render(
            'Tower Defense Troops', True, (0, 0, 0))
        td_rect = td_text.get_rect()
        td_rect.center = (td_upgrades.centerx, td_upgrades.bottom+25)

        pets_text = self.font1.render(
            'Pets', True, (0, 0, 0))
        pets_rect = pets_text.get_rect()
        pets_rect.center = (pets.centerx, pets.bottom+25)

        # buttons to go back and exit

        exit_text = self.font2.render("Exit", True,
                                      (255, 255, 255), (204, 51, 0))
        exit_rect = exit_text.get_rect()
        exit_rect.center = (40, 125)

        bg_rect = pygame.Rect(0, 0, 60, 30)
        bg_rect.center = exit_rect.center

        back_text = self.font2.render("Back", True,
                                      (255, 255, 255), (0, 0, 0))
        back_rect = back_text.get_rect()

        back_rect.center = (
            exit_rect.centerx, exit_rect.centery+exit_rect.width + 15)

        bge_rect = pygame.Rect(0, 0, 60, 30)
        bge_rect.center = back_rect.center

        def mainrender():

            self.main_screen.fill(bg_color)

            if self.curr_screen == 'main':  # current screen

                store_text = self.titleFont.render(
                    "Shop", True, (0, 0, 0))
                store_rect = store_text.get_rect()
                store_rect.center = (screenRectangle.centerx, 150)

                self.main_screen.blit(store_text, store_rect)
                pygame.draw.rect(self.main_screen, (150, 58, 38),
                                 weapon_upgrades)
                pygame.draw.rect(self.main_screen, (0, 0, 0),
                                 weapon_upgrades, width=2)

                pygame.draw.rect(self.main_screen, (32, 128, 40), td_upgrades)
                pygame.draw.rect(self.main_screen, (0, 0, 0),
                                 td_upgrades, width=2)

                pygame.draw.rect(self.main_screen, (50, 70, 168), pets)
                pygame.draw.rect(self.main_screen, (0, 0, 0), pets, width=2)

                self.main_screen.blit(weapon_text, weapon_rect)
                self.main_screen.blit(td_text, td_rect)

                self.main_screen.blit(pets_text, pets_rect)
                self.main_screen.blit(
                    pygame.transform.scale((self.ballista_img), (200, 200)), weapon_upgrades)
                self.main_screen.blit(pygame.transform.scale(
                    (self.green_dragon), (125, 125)), (pets.x+30, pets.y+25))

                pygame.draw.rect(self.main_screen, (204, 51, 0),
                                 bg_rect)
                self.main_screen.blit(exit_text, exit_rect)

            elif self.curr_screen == "troops":
                store_text = self.titleFont.render(
                    "Tower Defense Troops", True, (0, 0, 0))
                store_rect = store_text.get_rect()
                store_rect.center = (screenRectangle.centerx, 150)
                self.main_screen.blit(store_text, store_rect)

                self.main_screen.blit(self.tower_img, (468, 200))
                self.main_screen.blit(pygame.transform.scale(
                    self.pikeman_img, (160, 160)), (800, 200))

                self.td_items['towerHealth'].blitLabel(
                    self.main_screen, 550, 500)

                self.td_items['archerDamage'].blitLabel(
                    self.main_screen, 200, 500)

                self.td_items['archerAttackSpeed'].blitLabel(
                    self.main_screen, 200, 670)

                self.td_items['pikemanDamage'].blitLabel(
                    self.main_screen, 900, 500)

                self.td_items['pikemanAttackSpeed'].blitLabel(
                    self.main_screen, 900, 670)

                pygame.draw.rect(self.main_screen, (204, 51, 0), bg_rect)
                self.main_screen.blit(exit_text, exit_rect)
                pygame.draw.rect(self.main_screen, (0, 0, 0), bge_rect)
                self.main_screen.blit(back_text, back_rect)

            elif self.curr_screen == "weapons":

                store_text = self.titleFont.render(
                    "Tower Defense Weapons", True, (0, 0, 0))
                store_rect = store_text.get_rect()
                store_rect.center = (screenRectangle.centerx, 150)
                self.main_screen.blit(store_text, store_rect)

                self.main_screen.blit(pygame.transform.scale(
                    self.ballista_img, (250, 250)), (650, 140))

                self.main_screen.blit(pygame.transform.scale(
                    self.cannon_img, (300, 300)), (140, 125))

                self.td_items['ballistaProjectileHealth'].blitLabel(
                    self.main_screen, 780, 580)
                self.td_items['ballistaAttackSpeed'].blitLabel(
                    self.main_screen, 780, 450)

                self.td_items['cannonAttackSpeed'].blitLabel(
                    self.main_screen, 320, 450)
                self.td_items['cannonDamage'].blitLabel(
                    self.main_screen, 320, 580)
                self.td_items['cannonRange'].blitLabel(
                    self.main_screen, 320, 710)

                pygame.draw.rect(self.main_screen, (204, 51, 0), bg_rect)
                self.main_screen.blit(exit_text, exit_rect)
                pygame.draw.rect(self.main_screen, (0, 0, 0), bge_rect)
                self.main_screen.blit(back_text, back_rect)

            elif self.curr_screen == 'pets':

                store_text = self.titleFont.render(
                    "Dragons", True, (0, 0, 0))
                store_rect = store_text.get_rect()
                store_rect.center = (screenRectangle.centerx, 150)
                self.main_screen.blit(store_text, store_rect)

                self.main_screen.blit(pygame.transform.scale(
                    (self.pet_items['red'].image), (125, 125)), (490, 250))
                self.pBar.pet_items['red'].blitLabel(
                    self.main_screen, 550, 450)

                self.main_screen.blit(pygame.transform.scale(
                    (self.pet_items['green'].image), (125, 125)), (215, 250))
                self.pet_items['green'].blitLabel(self.main_screen, 275, 450)

                self.main_screen.blit(pygame.transform.scale(
                    (self.pet_items['purple'].image), (125, 125)), (765, 250))
                self.pet_items['purple'].blitLabel(self.main_screen, 825, 450)

                pygame.draw.rect(self.main_screen, (204, 51, 0),
                                 bg_rect)
                self.main_screen.blit(exit_text, exit_rect)

                pygame.draw.rect(self.main_screen, (0, 0, 0), bge_rect)

                self.main_screen.blit(back_text, back_rect)

        running = True
        while running:

            # Handle events
            events = pygame.event.get()

            self.pBar_g.update(events)
            pygame.display.flip()
            pygame.display.update()
            mainrender()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.WINDOWSHOWN:
                    for p in self.pBar_g:
                        p.setMessage(
                            ['Welcome to the store', 'You can purchase pets', ' or upgrade your character, weapons, and tower defenses'])

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if bg_rect.collidepoint(event.pos):
                        running = False

                    if self.curr_screen == 'main':

                        if pets.collidepoint(event.pos):
                            print("pets selected")
                            time.sleep(0.05)
                            self.curr_screen = 'pets'

                        elif weapon_upgrades.collidepoint(event.pos):
                            print("weapons selected")
                            time.sleep(0.05)
                            self.curr_screen = 'weapons'
                            #running = False

                        elif td_upgrades.collidepoint(event.pos):
                            time.sleep(0.05)
                            self.curr_screen = 'troops'

                    elif self.curr_screen == 'pets':

                        if bge_rect.collidepoint(event.pos):
                            self.curr_screen = 'main'

                        for key in self.pet_items:
                            if self.pet_items[key].rect.collidepoint(event.pos):
                                if(not self.pet_items[key].purchased):
                                    self.pBar.purchase_pet_item(key)
                                else:
                                    self.pBar.equip_pet_item(key)

                    elif self.curr_screen == 'troops':
                        if bge_rect.collidepoint(event.pos):
                            self.curr_screen = 'main'

                        for key in self.td_items:
                            if not (key.__contains__('cannon') or key.__contains__('ballista')):
                                if self.td_items[key].rect.collidepoint(event.pos):
                                    self.pBar.purchase_td_upgrade(key)

                        if bge_rect.collidepoint(event.pos):
                            self.curr_screen = 'main'

                        for key in self.td_items:
                            if self.td_items[key].rect.collidepoint(event.pos):
                                self.pBar.purchase_td_upgrade(key)

                    elif self.curr_screen == "weapons":
                        if bge_rect.collidepoint(event.pos):
                            self.curr_screen = 'main'

                        for key in self.td_items:
                            if key.__contains__('cannon') or key.__contains__('ballista'):
                                if self.td_items[key].rect.collidepoint(event.pos):
                                    self.pBar.purchase_td_upgrade(key)

        # pets, defense upgrades, playerUpgrades, weaponUpgrades

    def blitLabel(self, text, rect):
        self.main_screen.blit(text, rect)
        self.main_screen.blit(
            pygame.transform.scale((self.coin_img), (35, 35)), (rect.x-30, rect.y))

    def defenseUpgrades(self):
        screenRectangle = self.main_screen.get_rect()
        bg_color = ('#639c7a')
        self.main_screen.fill(bg_color)

        running = True
        while running:

            # Handle events
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            self.pBar_g.update(events)
            pygame.display.flip()
            pygame.display.update()

        return

    def playerUpgrades(self):
        return

    def pets(self):
        return

    def weaponUpgrades(self):
        return


pygame.init()

screen = pygame.display.set_mode((1100, 800))

shop = ShopMenu()

shop.mainMenu()

pygame.quit()
