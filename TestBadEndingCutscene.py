from ExplorationMode.Level import Level
import TowerDefenseMode.Exterior as Exterior
import pygame
from ExplorationMode.Player import Player

pygame.init()

screen = pygame.display.set_mode((1000,700))
screenRectangle = screen.get_rect()

pygame.display.set_caption("Intro Cutscene")
font = pygame.font.Font('ExplorationMode/Font/Enchanted Land.otf',40)
text_boxes = [
    "Oh no! You have failed to defend the castle and the walls have fallen!",
    "The Tree of Immortality is no longer safe from the enemy. The Kingdom is ruined!",
    "The End! (Ending 2/3)"
]

text_box_x = 100
text_box_y = 50
button_x = 500
button_y = 500
line_height = 30
line_y = text_box_y

# Render and blit each line of text
for text in text_boxes:
    # Split text into multiple lines if it is too long
    lines = []
    words = text.split()
    current_line = words.pop(0)
    for word in words:
        if font.size(current_line + ' ' + word)[0] < screen.get_width() - text_box_x * 2:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    # Render and blit each line
    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (text_box_x, line_y))
        line_y += line_height


    button_surface = font.render("Click here to Continue",True,(255,255,255))
    button_rect = button_surface.get_rect()
    button_rect.x = button_x
    button_rect.y = button_y
    
    screen.blit(button_surface,button_rect)
    pygame.display.update()

    clicked = False
    while not clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                clicked = True