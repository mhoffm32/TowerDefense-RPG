import pygame
# this file will allow us to play a beginning and an end of game cutscene.
# not done yet
def draw_text(screen,text,size,color,x,y):
    font = pygame.font.SysFont(None,size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
    screen.blit(text_surface,text_rect)

class IntroCutScene:
    def __init__(self,player):
        self.name = 'test'
        self.step = 0
        self.timer 