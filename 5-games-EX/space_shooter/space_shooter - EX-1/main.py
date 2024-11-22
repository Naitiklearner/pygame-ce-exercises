import pygame

# General Setup
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Title = pygame.display.set_caption('Learning Pygame')

running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw the game
    display_surface.fill('blue')
    pygame.display.update()

pygame.quit()