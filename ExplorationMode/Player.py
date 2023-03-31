import pygame
from Character import Character
import sys
import time

sys.path.append('../groupproject-team-99')


class Player(Character):
    def __init__(self, screen, progressBar, w, h, room=None):
        self.gender = 'male'
        self.skin = 'medium'
        self.hair = 'blonde'
        self.speed = 5
        self.screen = screen
        self.room = room

        super().__init__(100, 200, 'Images/girl/girl_mannequin_side.png')

        self.progressBar = progressBar
        self.pet = self.progressBar.pet

        #print(self.rect.width, self.rect.height)

        self.set_sprite_size(w, h)
        self.setSize(w, h)

        self.updateCharacter()

        #print(self.rect.width, self.rect.height)

    def setRoom(self, room):
        self.room = room

    def set_sprite_size(self, w, h):

        self.rect.width = w
        self.rect.height = h

        self.playerSize = (self.rect.width, self.rect.height)

        self.girlRightSprite = pygame.transform.scale(pygame.image.load(
            'Images/girl/girl_mannequin_side.png'), self.playerSize)
        self.girlLeftSprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
            'Images/girl/girl_mannequin_side.png'), self.playerSize), True, False)
        self.girlDownSprite = pygame.transform.scale(pygame.image.load(
            'Images/girl/girl_mannequin_forward.png'), self.playerSize)
        self.girlUpSprite = pygame.transform.scale(pygame.image.load(
            'Images/girl/girl_mannequin_back.png'), self.playerSize)

        self.boyRightSprite = pygame.transform.scale(pygame.image.load(
            'Images/boy/boy_mannequin_side_idle.png'), self.playerSize)
        self.boyLeftSprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
            'Images/boy/boy_mannequin_side_idle.png'), self.playerSize), True, False)
        self.boyDownSprite = pygame.transform.scale(pygame.image.load(
            'Images/boy/boy_mannequin_forward_idle.png'), self.playerSize)
        self.boyUpSprite = pygame.transform.scale(pygame.image.load(
            'Images/boy/boy_mannequin_back_idle.png'), self.playerSize)

        #self.setSize(300, 400)

        self.girlSprites = [self.girlUpSprite,
                            self.girlRightSprite, self.girlLeftSprite, self.girlDownSprite]
        self.boySprites = [self.boyUpSprite, self.boyRightSprite,
                           self.boyLeftSprite, self.boyDownSprite]

        self.sprite_index = 3

        self.image = self.boySprites[self.sprite_index]

        self.image = pygame.transform.scale(self.image, self.playerSize)

        #super().__init__(self.rect.x, self.rect.y, self.image)

        # male skin
        self.male_skin_colour_images_DOWN = {
            'light': pygame.image.load('Images/boy/skin/forward/boy_light_skin_forward.png').convert_alpha(),
            'medium': pygame.image.load('Images/boy/skin/forward/boy_medium_skin_forward.png').convert_alpha(),
            'dark': pygame.image.load('Images/boy/skin/forward/boy_dark_skin_forward.png').convert_alpha()
        }
        self.male_skin_colour_images_RIGHT = {
            'light': pygame.image.load('Images/boy/skin/side/boy_light_skin_side.png').convert_alpha(),
            'medium': pygame.image.load('Images/boy/skin/side/boy_medium_skin_side.png').convert_alpha(),
            'dark': pygame.image.load('Images/boy/skin/side/boy_dark_skin_side.png').convert_alpha()
        }
        self.male_skin_colour_images_LEFT = {
            'light': pygame.transform.flip(pygame.image.load('Images/boy/skin/side/boy_light_skin_side.png').convert_alpha(), True, False),
            'medium': pygame.transform.flip(pygame.image.load('Images/boy/skin/side/boy_medium_skin_side.png').convert_alpha(), True, False),
            'dark': pygame.transform.flip(pygame.image.load('Images/boy/skin/side/boy_dark_skin_side.png').convert_alpha(), True, False)
        }
        self.male_skin_colour_images_UP = {
            'light': pygame.image.load('Images/boy/skin/back/boy_light_skin_back.png').convert_alpha(),
            'medium': pygame.image.load('Images/boy/skin/back/boy_medium_skin_back.png').convert_alpha(),
            'dark': pygame.image.load('Images/boy/skin/back/boy_dark_skin_back.png').convert_alpha()
        }

        self.male_skin_images = [self.male_skin_colour_images_UP,
                                 self.male_skin_colour_images_RIGHT, self.male_skin_colour_images_LEFT,
                                 self.male_skin_colour_images_DOWN]

        # male hair
        self.male_hair_colour_images_DOWN = {
            'blonde': pygame.image.load('Images/boy/hair/forward/boy_blonde_hair_forward.png').convert_alpha(),
            'brown': pygame.image.load('Images/boy/hair/forward/boy_brown_hair_forward.png').convert_alpha(),
            'black': pygame.image.load('Images/boy/hair/forward/boy_black_hair_forward.png').convert_alpha()
        }
        self.male_hair_colour_images_RIGHT = {
            'blonde': pygame.image.load('Images/boy/hair/side/boy_blonde_hair_side.png').convert_alpha(),
            'brown': pygame.image.load('Images/boy/hair/side/boy_brown_hair_side.png').convert_alpha(),
            'black': pygame.image.load('Images/boy/hair/side/boy_black_hair_side.png').convert_alpha()
        }
        self.male_hair_colour_images_LEFT = {
            'blonde': pygame.transform.flip(pygame.image.load('Images/boy/hair/side/boy_blonde_hair_side.png').convert_alpha(), True, False),
            'brown': pygame.transform.flip(pygame.image.load('Images/boy/hair/side/boy_brown_hair_side.png').convert_alpha(), True, False),
            'black': pygame.transform.flip(pygame.image.load('Images/boy/hair/side/boy_black_hair_side.png').convert_alpha(), True, False)
        }
        self.male_hair_colour_images_UP = {
            'blonde': pygame.image.load('Images/boy/hair/back/boy_blonde_hair_back.png').convert_alpha(),
            'brown': pygame.image.load('Images/boy/hair/back/boy_brown_hair_back.png').convert_alpha(),
            'black': pygame.image.load('Images/boy/hair/back/boy_black_hair_back.png').convert_alpha()
        }

        self.male_hair_images = [self.male_hair_colour_images_UP,
                                 self.male_hair_colour_images_RIGHT, self.male_hair_colour_images_LEFT, self.male_hair_colour_images_DOWN]

        # female attriibutes

        # female skin
        self.female_skin_colour_images_DOWN = {
            'light': pygame.image.load('Images/girl/skin/forward/girl_light_skin_forward.png').convert_alpha(),
            'medium': pygame.image.load('Images/girl/skin/forward/girl_medium_skin_forward.png').convert_alpha(),
            'dark': pygame.image.load('Images/girl/skin/forward/girl_dark_skin_forward.png').convert_alpha()
        }
        self.female_skin_colour_images_RIGHT = {
            'light': pygame.image.load('Images/girl/skin/side/girl_light_skin_side.png').convert_alpha(),
            'medium': pygame.image.load('Images/girl/skin/side/girl_medium_skin_side.png').convert_alpha(),
            'dark': pygame.image.load('Images/girl/skin/side/girl_dark_skin_side.png').convert_alpha()
        }
        self.female_skin_colour_images_LEFT = {
            'light': pygame.transform.flip(pygame.image.load('Images/girl/skin/side/girl_light_skin_side.png').convert_alpha(), True, False),
            'medium': pygame.transform.flip(pygame.image.load('Images/girl/skin/side/girl_medium_skin_side.png').convert_alpha(), True, False),
            'dark': pygame.transform.flip(pygame.image.load('Images/girl/skin/side/girl_dark_skin_side.png').convert_alpha(), True, False)
        }
        self.female_skin_colour_images_UP = {
            'light': pygame.image.load('Images/girl/skin/back/girl_light_skin_back.png').convert_alpha(),
            'medium': pygame.image.load('Images/girl/skin/back/girl_medium_skin_back.png').convert_alpha(),
            'dark': pygame.image.load('Images/girl/skin/back/girl_dark_skin_back.png').convert_alpha()
        }
        self.female_skin_images = [self.female_skin_colour_images_UP,
                                   self.female_skin_colour_images_RIGHT, self.female_skin_colour_images_LEFT, self.female_skin_colour_images_DOWN]

        self.female_hair_colour_images_DOWN = {
            'blonde': pygame.image.load('Images/girl/hair/forward/girl_blonde_hair_forward.png').convert_alpha(),
            'brown': pygame.image.load('Images/girl/hair/forward/girl_brown_hair_forward.png').convert_alpha(),
            'black': pygame.image.load('Images/girl/hair/forward/girl_black_hair_forward.png').convert_alpha()
        }
        self.female_hair_colour_images_RIGHT = {
            'blonde': pygame.image.load('Images/girl/hair/side/girl_blonde_hair_side.png').convert_alpha(),
            'brown': pygame.image.load('Images/girl/hair/side/girl_brown_hair_side.png').convert_alpha(),
            'black': pygame.image.load('Images/girl/hair/side/girl_black_hair_side.png').convert_alpha()
        }
        self.female_hair_colour_images_LEFT = {
            'blonde': pygame.transform.flip(pygame.image.load('Images/girl/hair/side/girl_blonde_hair_side.png').convert_alpha(), True, False),
            'brown': pygame.transform.flip(pygame.image.load('Images/girl/hair/side/girl_brown_hair_side.png').convert_alpha(), True, False),
            'black': pygame.transform.flip(pygame.image.load('Images/girl/hair/side/girl_black_hair_side.png').convert_alpha(), True, False)
        }
        self.female_hair_colour_images_UP = {
            'blonde': pygame.image.load('Images/girl/hair/back/girl_blonde_hair_back.png').convert_alpha(),
            'brown': pygame.image.load('Images/girl/hair/back/girl_brown_hair_back.png').convert_alpha(),
            'black': pygame.image.load('Images/girl/hair/back/girl_black_hair_back.png').convert_alpha()
        }

        self.female_hair_images = [self.female_hair_colour_images_UP,
                                   self.female_hair_colour_images_RIGHT, self.female_hair_colour_images_LEFT, self.female_hair_colour_images_DOWN]

    def hasPet(self):
        if not (self.progressBar.pet == None):
            self.pet = self.progressBar.pet
            return True
        else:
            return False

    def get_pet_img(self):
        if(self.sprite_index == 2) or (self.sprite_index == 3):
            return self.pet.l_image

        elif(self.sprite_index == 1) or (self.sprite_index == 0):
            return self.pet.r_image

    def updateCharacter(self):

        # updating female hair
        self.female_hair_dict = self.female_hair_images[self.sprite_index]
        self.female_hair_img = self.female_hair_dict[self.hair]

        # updating female skin
        self.female_skin_dict = self.female_skin_images[self.sprite_index]
        self.female_skin_img = self.female_skin_dict[self.skin]

        # updating male skin
        self.male_skin_dict = self.male_skin_images[self.sprite_index]
        self.male_skin_img = self.male_skin_dict[self.skin]

        # updating male hair
        self.male_hair_dict = self.male_hair_images[self.sprite_index]
        self.male_hair_img = self.male_hair_dict[self.hair]

        if self.gender == 'female':
            self.image = self.girlSprites[self.sprite_index]

            self.female_hair_img = pygame.transform.scale(
                self.female_hair_img, (self.rect.width, self.rect.height))
            self.image.blit(self.female_hair_img, (0, 0))

            self.female_skin_img = pygame.transform.scale(
                self.female_skin_img, (self.rect.width, self.rect.height))
            self.image.blit(self.female_skin_img, (0, 0))

        elif self.gender == 'male':

            self.image = self.boySprites[self.sprite_index]

            self.male_hair_img = pygame.transform.scale(
                self.male_hair_img, self.playerSize)

            self.image.blit(self.male_hair_img, (0, 0))

            self.male_skin_img = pygame.transform.scale(
                self.male_skin_img, self.playerSize)

            self.image.blit(self.male_skin_img, (0, 0))

        if self.hasPet():
            self.pet_img = self.get_pet_img()
            self.screen.blit(self.pet_img, self.rect.topright)

        super().update_img(self.image)

        #self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.move()
        self.updateCharacter()

    def updatePosition(self):
        self.move()

    def setPosition(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def setSize(self, w, h):
        self.rect.width = w
        self.rect.height = h

        self.playerSize = (self.rect.width, self.rect.height)

        #self.load_sprites(w, h)
        #super().__init__(self.rect.x, self.rect.y, self.image)

    def move(self):
        # move the player
        keysPressed = pygame.key.get_pressed()

        if(keysPressed[pygame.K_LEFT]):
            self.rect.x -= self.speed
            self.sprite_index = 2

        if(keysPressed[pygame.K_RIGHT]):
            self.rect.x += self.speed
            self.sprite_index = 1

        if(keysPressed[pygame.K_UP]):
            self.rect.y -= self.speed
            self.sprite_index = 0

        if(keysPressed[pygame.K_DOWN]):
            self.rect.y += self.speed
            self.sprite_index = 3

        # self.rect.move_ip(self.rect.x,self.rect.y)

        # if the result of the move puts the player in a wall: revert movement

        if self.room.checkCollision():
            if(keysPressed[pygame.K_LEFT]):
                self.rect.x += self.speed
            if(keysPressed[pygame.K_RIGHT]):
                self.rect.x -= self.speed
            if(keysPressed[pygame.K_UP]):
                self.rect.y += self.speed
            if(keysPressed[pygame.K_DOWN]):
                self.rect.y -= self.speed

    def setAttributes(self, gender, skin, hair):
        self.gender = gender
        self.skin = skin
        self.hair = hair

    def collectItem(self, item):
        self.progressBar.add_coin(item.moneyValue)
        self.progressBar.add_diamond(item.crystalValue)
        self.progressBar.update_xp(item.xpValue)

    def customize(self):
        pygame.init()

        screen = pygame.display.set_mode((1000, 700))
        screenRectangle = screen.get_rect()

        bg_color = ('#639c7a')
        screen.fill(bg_color)

        playerGroup = pygame.sprite.Group()
        player = Player(screen, self.progressBar, 400, 600)

        self.sprite_index = 3

        self.setPosition((80, 50))

        playerGroup.add(player)
        playerGroup.draw(screen)

        font = pygame.font.SysFont('Times', 20)
        font2 = pygame.font.SysFont('Times', 30)

        light_skin = pygame.Rect(750, 300, 50, 50)
        medium_skin = pygame.Rect(810, 300, 50, 50)
        dark_skin = pygame.Rect(870, 300, 50, 50)

        skin_text = font.render(
            'Please Choose Your Skin Tone:', True, (0, 0, 0))
        skin_rect = skin_text.get_rect()
        skin_rect.center = (830, 270)

        blonde_hair = pygame.Rect(750, 420, 50, 50)
        brown_hair = pygame.Rect(810, 420, 50, 50)
        black_hair = pygame.Rect(870, 420, 50, 50)

        hair_text = font.render(
            'Please Choose Your Hair Colour:', True, (0, 0, 0))
        hair_rect = hair_text.get_rect()
        hair_rect.center = (830, 390)

        male_text = font2.render('Male', True, (225, 225, 225))
        male_rect = male_text.get_rect()
        male_rect.center = (750, 210)

        female_text = font2.render('Female', True, (225, 225, 225))
        female_rect = female_text.get_rect()
        female_rect.center = (890, 210)

        gender_text = font.render(
            'Please Select Your Gender: ', True, (0, 0, 0))
        gender_rect = gender_text.get_rect()
        gender_rect.center = (830, 150)

        save_text = font.render("Save Character", True,
                                (255, 255, 255), (0, 0, 0))
        save_rect = save_text.get_rect()
        save_rect.center = (835, 600)
        save_bg = pygame.draw.rect(
            screen, (0, 0, 0), pygame.Rect(650, 500, 140, 40))
        save_bg.center = save_rect.center

        def render():

            screen.blit(skin_text, skin_rect)
            screen.blit(hair_text, hair_rect)
            screen.blit(male_text, male_rect)
            screen.blit(female_text, female_rect)
            screen.blit(gender_text, gender_rect)
            # screen.blit(save_text, save_rect)

            pygame.draw.rect(screen, (0, 0, 0), save_bg)
            screen.blit(save_text, save_rect)

            pygame.draw.rect(screen, '#f1e3d0', light_skin)
            pygame.draw.rect(screen, (0, 0, 0), light_skin, width=2)
            pygame.draw.rect(screen, '#9b7e64', medium_skin)
            pygame.draw.rect(screen, (0, 0, 0), medium_skin, width=2)
            pygame.draw.rect(screen, '#4b3009', dark_skin)
            pygame.draw.rect(screen, (0, 0, 0), dark_skin, width=2)
            pygame.draw.rect(screen, '#c0a648', blonde_hair)
            pygame.draw.rect(screen, (0, 0, 0), blonde_hair, width=2)
            pygame.draw.rect(screen, '#7f580e', brown_hair)
            pygame.draw.rect(screen, (0, 0, 0), brown_hair, width=2)
            pygame.draw.rect(screen, '#0f0b02', black_hair)
            pygame.draw.rect(screen, (0, 0, 0), black_hair, width=2)

            button_surface = font.render("Finish", True, (255, 255, 255))
            button_rect = button_surface.get_rect()
            button_rect.x = 700
            button_rect.y = 700

        '''self.gender = 'male'
        hair = 'blonde'
        skin = 'light'''

        # Main game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a rectangle was clicked
                    if save_bg.collidepoint(event.pos):
                        print('saved')
                        time.sleep(0.5)
                        running = False
                    elif male_rect.collidepoint(event.pos):
                        self.gender = 'male'
                        print('Male chosen!')
                        # remove the old player sprite
                        # playerGroup.remove(player)
                    elif female_rect.collidepoint(event.pos):
                        self.gender = 'female'
                        # remove the old player sprite
                       # playerGroup.remove(player)
                        print('Female chosen!')
                    if light_skin.collidepoint(event.pos):
                        # set player's skin to light
                        self.skin = 'light'
                        print('Light skin chosen!')
                    elif medium_skin.collidepoint(event.pos):
                        # set player's skin to medium
                        self.skin = 'medium'
                        print('Medium skin chosen!')
                    elif dark_skin.collidepoint(event.pos):
                        # set player's skin to dark
                        self.skin = 'dark'
                        print('Dark skin chosen!')
                    elif blonde_hair.collidepoint(event.pos):
                        # set player's hair to blonde
                        self.hair = 'blonde'
                        print('Blonde hair chosen!')
                    elif brown_hair.collidepoint(event.pos):
                        # set player's hair to brown
                        self.hair = 'brown'
                        print('Brown hair chosen!')
                    elif black_hair.collidepoint(event.pos):
                        # set player's hair to black
                        self.hair = 'black'
                        print('Black hair chosen!')

            self.updateCharacter()
            screen.fill(bg_color)
            render()
            # Update the screen
            playerGroup.empty()
            playerGroup.add(self)  # add the new player sprite
            playerGroup.draw(screen)
            pygame.display.flip()

        gamePlayer = Player(self.screen, self.progressBar, 50, 70)
        gamePlayer.gender = self.gender
        gamePlayer.skin = self.skin
        gamePlayer.hair = self.hair
        self.progressBar.set_player(gamePlayer)
        return gamePlayer
        # Quit Pygame

pygame.init()


# here we can add customizable features with different img urls for
# different characters depending on gender, hair color, etc'''
# '''customizable name that we can use throughout the game'''
