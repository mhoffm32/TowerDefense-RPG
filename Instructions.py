import pygame
import time

class Instructions():
    def __init__(self, surface):
        self.screen = surface
        self.run = True
    def runScene(self):
        pygame.init()

        screen = pygame.display.set_mode((1000, 700))
        screenRectangle = screen.get_rect()
        
        bg = pygame.image.load('Images/backgrounds/INSTRUCTIONS.png')
        self.screen.blit(bg,(0,0))

        font = pygame.font.SysFont('Times', 20)
        button_x = 70
        button_y = 70

        button_surface = font.render("Click here to Continue",True,(255,255,255))
        button_rect = button_surface.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y

        self.screen.blit(button_surface,button_rect)
        pygame.display.update()

        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                    print("instructions closed")
                    screen.fill((0,0,0))
                    running = False
                    self.run = False
                    time.sleep(0.5)
