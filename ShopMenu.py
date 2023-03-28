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
            'ExplorationMode/Font/Enchanted Land.otf', 50)

        self.font2 = pygame.font.Font(
            'ExplorationMode/Font/Enchanted Land.otf', 30)

        self.green_dragon = pygame.image.load(
            'Images/dragons/greendragon.png')
        self.purple_dragon = pygame.image.load(
            'Images/dragons/purpledragon.png')
        self.red_dragon = pygame.image.load('Images/dragons/reddragon.png')

        self.bow_img = pygame.image.load('Images/weapons/bow_arrow_sprite.png')

        self.coin_img = pygame.image.load('Images/coin.png')

    def mainMenu(self):
        screenRectangle = self.main_screen.get_rect()

        bg_color = ('#639c7a')
        self.main_screen.fill(bg_color)

        # main screen stuff

        store_text = self.font1.render(
            'Welcome to the store', True, (0, 0, 0))
        store_rect = store_text.get_rect()
        store_rect.center = (screenRectangle.centerx, 100)

        weapon_upgrades = pygame.Rect(275, 150, 200, 200)
        td_upgrades = pygame.Rect(625, 150, 200, 200)
        player_upgrades = pygame.Rect(275, 450, 200, 200)
        pets = pygame.Rect(625, 450, 200, 200)

        weapon_text = self.font2.render(
            'Weapons', True, (0, 0, 0))
        weapon_rect = weapon_text.get_rect()
        weapon_rect.center = (weapon_upgrades.centerx, 365)

        td_text = self.font2.render(
            'Tower Defense Upgrades', True, (0, 0, 0))
        td_rect = td_text.get_rect()
        td_rect.center = (td_upgrades.centerx, 365)

        player_text = self.font2.render(
            'Player Upgrades', True, (0, 0, 0))
        player_rect = player_text.get_rect()
        player_rect.center = (player_upgrades.centerx, 665)

        pets_text = self.font2.render(
            'Pets', True, (0, 0, 0))
        pets_rect = pets_text.get_rect()
        pets_rect.center = (pets.centerx, 665)

        # buttons to go back and exit

        exit_text = self.font2.render("Exit", True,
                                      (255, 255, 255), (204, 51, 0))
        exit_rect = exit_text.get_rect()
        exit_rect.center = (100, 125)

        bg_rect = pygame.Rect(0, 0, 140, 40)
        bg_rect.center = exit_rect.center

        back_text = self.font2.render("Back", True,
                                      (255, 255, 255), (0, 0, 0))
        back_rect = back_text.get_rect()

        back_rect.center = (
            exit_rect.centerx, exit_rect.centery+exit_rect.width + 15)

        bge_rect = pygame.Rect(0, 0, 140, 40)
        bge_rect.center = back_rect.center

        def mainrender():

            self.main_screen.fill(bg_color)

            if self.curr_screen == 'main':  # current screen
                pygame.draw.rect(self.main_screen, '#f1e3d0',
                                 weapon_upgrades)
                pygame.draw.rect(self.main_screen, (0, 0, 0),
                                 weapon_upgrades, width=2)

                pygame.draw.rect(self.main_screen, '#9b7e64', td_upgrades)
                pygame.draw.rect(self.main_screen, (0, 0, 0),
                                 td_upgrades, width=2)

                pygame.draw.rect(self.main_screen, (50, 70, 168), pets)
                pygame.draw.rect(self.main_screen, (0, 0, 0), pets, width=2)

                pygame.draw.rect(self.main_screen, '#c0a648',
                                 player_upgrades)
                pygame.draw.rect(self.main_screen, (0, 0, 0),
                                 player_upgrades, width=2)

                self.main_screen.blit(weapon_text, weapon_rect)
                self.main_screen.blit(td_text, td_rect)
                self.main_screen.blit(player_text, player_rect)
                self.main_screen.blit(pets_text, pets_rect)
                self.main_screen.blit(
                    pygame.transform.scale((self.bow_img), (150, 150)), (weapon_upgrades.x+20, weapon_upgrades.y+20))
                self.main_screen.blit(pygame.transform.scale(
                    (self.red_dragon), (125, 125)), (pets.x+25, pets.y+25))

                pygame.draw.rect(self.main_screen, (204, 51, 0),
                                 bg_rect)
                self.main_screen.blit(exit_text, exit_rect)

            elif self.curr_screen == "td":

                self.td_items['archerDamage'].blitLabel(
                    self.main_screen, 300, 300)
                self.td_items['archerAttackSpeed'].blitLabel(
                    self.main_screen, 600, 300)
                self.td_items['pikemanDamage'].blitLabel(
                    self.main_screen, 900, 300)

                pygame.draw.rect(self.main_screen, (204, 51, 0), bg_rect)
                self.main_screen.blit(exit_text, exit_rect)
                pygame.draw.rect(self.main_screen, (0, 0, 0), bge_rect)
                self.main_screen.blit(back_text, back_rect)

            elif self.curr_screen == 'pets':

                self.main_screen.blit(pygame.transform.scale(
                    (self.pet_items['red'].image), (125, 125)), (500, 200))
                self.pBar.pet_items['red'].blitLabel(
                    self.main_screen, 550, 400)

                self.main_screen.blit(pygame.transform.scale(
                    (self.pet_items['green'].image), (125, 125)), (225, 200))
                self.pet_items['green'].blitLabel(self.main_screen, 275, 400)

                self.main_screen.blit(pygame.transform.scale(
                    (self.pet_items['purple'].image), (125, 125)), (775, 200))
                self.pet_items['purple'].blitLabel(self.main_screen, 825, 400)

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
                            #running = False

                        elif td_upgrades.collidepoint(event.pos):
                            print("Tower defense upgrades")
                            time.sleep(0.05)
                            self.curr_screen = 'td'

                        elif player_upgrades.collidepoint(event.pos):
                            print("Player upgrades")
                            time.sleep(0.05)

                    elif self.curr_screen == 'pets':

                        if bge_rect.collidepoint(event.pos):
                            self.curr_screen = 'main'

                        for key in self.pet_items:
                            if self.pet_items[key].rect.collidepoint(event.pos):
                                if(not self.pet_items[key].purchased):
                                    self.pBar.purchase_pet_item(key)
                                else:
                                    self.pBar.equip_pet_item(key)

                    elif self.curr_screen == 'td':
                        if bge_rect.collidepoint(event.pos):
                            self.curr_screen = 'main'

                        for key in self.td_items:
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
