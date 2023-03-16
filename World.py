from ExplorationMode.Level import Level
import TowerDefenseMode.Exterior as Exterior
import pygame

pygame.init()

screen = pygame.display.set_mode((1000,700))
screenRectangle = screen.get_rect()

level = Level(screen)

# i am commenting this so it doesnt get in everyones way during testing!
# uncomment to see the effect by putting a hashtag in front of the triple quotes on both ends.
# please recomment them after so that people can test without having the introduction in the way.
"""
pygame.display.set_caption("Intro Cutscene")
font = pygame.font.SysFont('ExplorationMode\Font\Minecraft.ttf',30)
text_boxes = [
    "Welcome to The Immortal Garden.",
    "You are the King/Queen of this kingdom. Your job is to protect the Tree of Immortality from the enemy army!",
    "You will have time to first explore the castle town. Once the timer reaches zero, you must be ready to \ndefend the castle walls to prevent them from being breached!",
    "After each wave of enemies, you will have the chance to explore the castle town once again. Good luck!"
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
"""                

running = True
while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.update()
    pygame.display.flip()
    screen.fill((0,0,0))

pygame.quit()
