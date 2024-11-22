import pygame

# General Setup
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Title = pygame.display.set_caption('Learning Pygame')

running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw the game
    Screen.fill('blue')
    pygame.display.update()

pygame.quit()