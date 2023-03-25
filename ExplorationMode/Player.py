import pygame
from Character import Character
import sys

sys.path.append('../groupproject-team-99')


class Player(Character):
    def __init__(self, screen, progressBar):
        super().__init__(500, 500, 'Images/boy/boy_mannequin_side_idle.png')
        self.gender = 'male'
        self.skin = 'medium'
        self.hair = 'brown'
        self.gender = 'male'

        self.playerWidth = 50
        self.playerHeight = 70
        self.playerSize = (self.playerWidth, self.playerHeight)

        self.girlSideSprite = pygame.transform.scale(pygame.image.load(
            'Images/girl/girl_mannequin_side.png'), self.playerSize)
        self.girlDownSprite = pygame.transform.scale(pygame.image.load(
            'Images/girl/girl_mannequin_forward.png'), self.playerSize)
        self.girlUpSprite = pygame.transform.scale(pygame.image.load(
            'Images/girl/girl_mannequin_back.png'), self.playerSize)

        self.boySideSprite = pygame.transform.scale(pygame.image.load(
            'Images/boy/boy_mannequin_side_idle.png'), self.playerSize)
        self.boyDownSprite = pygame.transform.scale(pygame.image.load(
            'Images/boy/boy_mannequin_forward_idle.png'), self.playerSize)
        self.boyUpSprite = pygame.transform.scale(pygame.image.load(
            'Images/boy/boy_mannequin_back_idle.png'), self.playerSize)

        self.girlSprites = [self.girlUpSprite,
                            self.girlSideSprite, self.girlDownSprite]
        self.boySprites = [self.boyUpSprite,
                           self.boySideSprite, self.boyDownSprite]

        self.sprite_index = 2

        self.image = self.boySprites[self.sprite_index]

        self.image = pygame.transform.scale(self.image, self.playerSize)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300

        self.speed = 5
        self.screen = screen
        '''self.room = room'''
        self.progressBar = progressBar

        # male skin
        self.male_skin_colour_images_DOWN = {
            'light': pygame.image.load('Images/boy/skin/forward/boy_light_skin_forward.png').convert_alpha(),
            'medium': pygame.image.load('Images/boy/skin/forward/boy_medium_skin_forward.png').convert_alpha(),
            'dark': pygame.image.load('Images/boy/skin/forward/boy_dark_skin_forward.png').convert_alpha()
        }
        self.male_skin_colour_images_SIDE = {
            'light': pygame.image.load('Images/boy/skin/side/boy_light_skin_side.png').convert_alpha(),
            'medium': pygame.image.load('Images/boy/skin/side/boy_medium_skin_side.png').convert_alpha(),
            'dark': pygame.image.load('Images/boy/skin/side/boy_dark_skin_side.png').convert_alpha()
        }
        self.male_skin_colour_images_UP = {
            'light': pygame.image.load('Images/boy/skin/back/boy_light_skin_back.png').convert_alpha(),
            'medium': pygame.image.load('Images/boy/skin/back/boy_medium_skin_back.png').convert_alpha(),
            'dark': pygame.image.load('Images/boy/skin/back/boy_dark_skin_back.png').convert_alpha()
        }

        self.male_skin_images = [self.male_skin_colour_images_UP,
                                 self.male_skin_colour_images_SIDE, self.male_skin_colour_images_DOWN]

        # male hair
        self.male_hair_colour_images_DOWN = {
            'blonde': pygame.image.load('Images/boy/hair/forward/boy_blonde_hair_forward.png').convert_alpha(),
            'brown': pygame.image.load('Images/boy/hair/forward/boy_brown_hair_forward.png').convert_alpha(),
            'black': pygame.image.load('Images/boy/hair/forward/boy_black_hair_forward.png').convert_alpha()
        }
        self.male_hair_colour_images_SIDE = {
            'blonde': pygame.image.load('Images/boy/hair/side/boy_blonde_hair_side.png').convert_alpha(),
            'brown': pygame.image.load('Images/boy/hair/side/boy_brown_hair_side.png').convert_alpha(),
            'black': pygame.image.load('Images/boy/hair/side/boy_black_hair_side.png').convert_alpha()
        }
        self.male_hair_colour_images_UP = {
            'blonde': pygame.image.load('Images/boy/hair/back/boy_blonde_hair_back.png').convert_alpha(),
            'brown': pygame.image.load('Images/boy/hair/back/boy_brown_hair_back.png').convert_alpha(),
            'black': pygame.image.load('Images/boy/hair/back/boy_black_hair_back.png').convert_alpha()
        }

        self.male_hair_images = [self.male_hair_colour_images_UP,
                                 self.male_hair_colour_images_SIDE, self.male_hair_colour_images_DOWN]

        # female attriibutes

        # female skin
        self.female_skin_colour_images_DOWN = {
            'light': pygame.image.load('Images/girl/skin/forward/girl_light_skin_forward.png').convert_alpha(),
            'medium': pygame.image.load('Images/girl/skin/forward/girl_medium_skin_forward.png').convert_alpha(),
            'dark': pygame.image.load('Images/girl/skin/forward/girl_dark_skin_forward.png').convert_alpha()
        }
        self.female_skin_colour_images_SIDE = {
            'light': pygame.image.load('Images/girl/skin/side/girl_light_skin_side.png').convert_alpha(),
            'medium': pygame.image.load('Images/girl/skin/side/girl_medium_skin_side.png').convert_alpha(),
            'dark': pygame.image.load('Images/girl/skin/side/girl_dark_skin_side.png').convert_alpha()
        }
        self.female_skin_colour_images_UP = {
            'light': pygame.image.load('Images/girl/skin/back/girl_light_skin_back.png').convert_alpha(),
            'medium': pygame.image.load('Images/girl/skin/back/girl_medium_skin_back.png').convert_alpha(),
            'dark': pygame.image.load('Images/girl/skin/back/girl_dark_skin_back.png').convert_alpha()
        }
        self.female_skin_images = [self.female_skin_colour_images_UP,
                                   self.female_skin_colour_images_SIDE, self.female_skin_colour_images_DOWN]

        self.female_hair_colour_images_DOWN = {
            'blonde': pygame.image.load('Images/girl/hair/forward/girl_blonde_hair_forward.png').convert_alpha(),
            'brown': pygame.image.load('Images/girl/hair/forward/girl_brown_hair_forward.png').convert_alpha(),
            'black': pygame.image.load('Images/girl/hair/forward/girl_black_hair_forward.png').convert_alpha()
        }
        self.female_hair_colour_images_SIDE = {
            'blonde': pygame.image.load('Images/girl/hair/side/girl_blonde_hair_side.png').convert_alpha(),
            'brown': pygame.image.load('Images/girl/hair/side/girl_brown_hair_side.png').convert_alpha(),
            'black': pygame.image.load('Images/girl/hair/side/girl_black_hair_side.png').convert_alpha()
        }
        self.female_hair_colour_images_UP = {
            'blonde': pygame.image.load('Images/girl/hair/back/girl_blonde_hair_back.png').convert_alpha(),
            'brown': pygame.image.load('Images/girl/hair/back/girl_brown_hair_back.png').convert_alpha(),
            'black': pygame.image.load('Images/girl/hair/back/girl_black_hair_back.png').convert_alpha()
        }

        self.female_hair_images = [self.female_hair_colour_images_UP,
                                   self.female_hair_colour_images_SIDE, self.female_hair_colour_images_DOWN]

    def updateCharacter(self, surface):

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
                self.male_hair_img, (self.rect.width, self.rect.height))

            self.image.blit(self.male_hair_img, (0, 0))

            self.image = pygame.transform.scale(
                self.image, (self.rect.width, self.rect.height))
            self.male_skin_img = pygame.transform.scale(
                self.male_skin_img, (self.rect.width, self.rect.height))
            self.image.blit(self.male_skin_img, (0, 0))
            
        self.screen.blit(self.image,(400,400))

    def updatePosition(self):
        self.move()

    def setPosition(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def setSize(self, width, height):
        self.playerWidth = width
        self.playerHeight = height

    def move(self):
        # move the player
        keysPressed = pygame.key.get_pressed()
        if(keysPressed[pygame.K_LEFT]):
            self.rect.x -= self.speed
            self.sprite_index = 1

        if(keysPressed[pygame.K_RIGHT]):
            self.rect.x += self.speed
            self.sprite_index = 1

        if(keysPressed[pygame.K_UP]):
            self.rect.y -= self.speed
            self.sprite_index = 0

        if(keysPressed[pygame.K_DOWN]):
            self.rect.y += self.speed
            self.sprite_index = 2

        # if the result of the move puts the player in a wall: revert movement
        '''if self.room.checkCollision():
            if(keysPressed[pygame.K_LEFT]):
                self.rect.x += self.speed
            if(keysPressed[pygame.K_RIGHT]):
                self.rect.x -= self.speed
            if(keysPressed[pygame.K_UP]):
                self.rect.y += self.speed
            if(keysPressed[pygame.K_DOWN]):
                self.rect.y -= self.speed'''

    '''def updateImage(self, gender, hair_colour, skin_colour):
        self.boySprite = pygame.image.load(
            'Images/boy/boy_mannequin_forward_idle.png')
        self.girlSprite = pygame.image.load(
            'Images/girl/girl_mannequin_forward.png')

        if gender == 'male':

            self.image = self.boySprites[self.sprite_index]
        
            # blitting the forward facing hair and skin colours onto male mannequin

            self.image = pygame.transform.scale(
                self.image, (self.rect.width, self.rect.height))


            self.male_skin_colour_images[skin_colour] = pygame.transform.scale(
                self.male_skin_colour_images[skin_colour], (self.rect.width, self.rect.height))

            self.image.blit(self.male_skin_colour_images[skin_colour], (0, 0))
            self.male_hair_colour_images[hair_colour] = pygame.transform.scale(
                self.male_hair_colour_images[hair_colour], (self.rect.width, self.rect.height))
    
            
            self.image.blit(self.male_hair_colour_images[hair_colour], (0, 0))


            self.sideSprite = pygame.transform.scale(
                self.sideSprite, (self.rect.width, self.rect.height))
            self.male_skin_colour_images_SIDE[skin_colour] = pygame.transform.scale(
                self.male_skin_colour_images_SIDE[skin_colour], (self.rect.width, self.rect.height))
            self.sideSprite.blit(
                self.male_skin_colour_images_SIDE[skin_colour], (0, 0))
            self.male_hair_colour_images_SIDE[hair_colour] = pygame.transform.scale(
                self.male_hair_colour_images_SIDE[hair_colour], (self.rect.width, self.rect.height))
            self.image.blit(
                self.male_hair_colour_images_SIDE[hair_colour], (0, 0))

        elif gender == 'female':
            # blitting the forward facing hair and skin colours onto female mannequin
            self.image = pygame.transform.scale(
                self.girlSprite, (self.rect.width, self.rect.height))
            self.female_skin_colour_images[skin_colour] = pygame.transform.scale(
                self.female_skin_colour_images[skin_colour], (self.rect.width, self.rect.height))
            self.image.blit(
                self.female_skin_colour_images[skin_colour], (0, 0))
            self.female_hair_colour_images[hair_colour] = pygame.transform.scale(
                self.female_hair_colour_images[hair_colour], (self.rect.width, self.rect.height))
            self.image.blit(
                self.female_hair_colour_images[hair_colour], (0, 0))'''

    def collectItem(self, item):
        self.progressBar.add_coin(item.moneyValue)
        self.progressBar.add_diamond(item.crystalValue)

    def getPlayerMenu(self):

        pygame.init()

        #screen = pygame.display.set_mode((800, 600))
        screenRectangle = self.screen.get_rect()

        bg_color = ('#639c7a')
        self.screen.fill(bg_color)

        playerGroup = pygame.sprite.Group()
        player = Player(self.screen, self.progressBar)

        player.sprite_index = 2

        player.rect.left = 80
        player.rect.top = 50
        player.rect.height = 360
        player.rect.width = 260

        player.image = pygame.transform.scale(player.image, (260, 360))

        playerGroup.add(player)
        playerGroup.draw(self.screen)

        font = pygame.font.SysFont('Times', 20)
        font2 = pygame.font.SysFont('Times', 30)

        light_skin = pygame.Rect(550, 200, 50, 50)
        medium_skin = pygame.Rect(610, 200, 50, 50)
        dark_skin = pygame.Rect(670, 200, 50, 50)

        skin_text = font.render(
            'Please Choose Your Skin Tone:', True, (0, 0, 0))
        skin_rect = skin_text.get_rect()
        skin_rect.center = (630, 170)

        blonde_hair = pygame.Rect(550, 320, 50, 50)
        brown_hair = pygame.Rect(610, 320, 50, 50)
        black_hair = pygame.Rect(670, 320, 50, 50)

        hair_text = font.render(
            'Please Choose Your Hair Colour:', True, (0, 0, 0))
        hair_rect = hair_text.get_rect()
        hair_rect.center = (630, 290)

        male_text = font2.render('Male', True, (225, 225, 225))
        male_rect = male_text.get_rect()
        male_rect.center = (550, 110)

        female_text = font2.render('Female', True, (225, 225, 225))
        female_rect = female_text.get_rect()
        female_rect.center = (690, 110)

        gender_text = font.render(
            'Please Select Your Gender: ', True, (0, 0, 0))
        gender_rect = gender_text.get_rect()
        gender_rect.center = (630, 50)

        save_text = font.render("Save Character", True,
                                (255, 255, 255), (0, 0, 168))
        save_rect = save_text.get_rect()
        save_rect.center = (630, 500)
        save_bg = pygame.draw.rect(
            self.screen, (0, 0, 168), pygame.Rect(650, 500, 140, 40))
        save_bg.center = save_rect.center

        def render():

            self.screen.blit(skin_text, skin_rect)
            self.screen.blit(hair_text, hair_rect)
            self.screen.blit(male_text, male_rect)
            self.screen.blit(female_text, female_rect)
            self.screen.blit(gender_text, gender_rect)
            #screen.blit(save_text, save_rect)

            pygame.draw.rect(self.screen, (0, 0, 168), save_bg)
            self.screen.blit(save_text, save_rect)

            pygame.draw.rect(self.screen, '#f1e3d0', light_skin)
            pygame.draw.rect(self.screen, '#9b7e64', medium_skin)
            pygame.draw.rect(self.screen, '#4b3009', dark_skin)
            pygame.draw.rect(self.screen, '#c0a648', blonde_hair)
            pygame.draw.rect(self.screen, '#7f580e', brown_hair)
            pygame.draw.rect(self.screen, '#0f0b02', black_hair)

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
                    elif male_rect.collidepoint(event.pos):
                        self.gender = 'male'
                        print('Male chosen!')
                        # remove the old player sprite
                        playerGroup.remove(player)
                    elif female_rect.collidepoint(event.pos):
                        self.gender = 'female'
                        # remove the old player sprite
                        playerGroup.remove(player)
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

            self.screen.fill(bg_color)
            render()
            # Update the screen
            playerGroup.empty()
            playerGroup.add(player)  # add the new player sprite
            playerGroup.draw(self.screen)
            self.updateCharacter(self.screen)
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()


pygame.init()


# here we can add customizable features with different img urls for
# different characters depending on gender, hair color, etc'''
#'''customizable name that we can use throughout the game'''
