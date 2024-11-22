import pygame
from os.path import join

from random import randint
# General Setup
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

Title = pygame.display.set_caption('Learning Pygame')

running = True

player_direction = pygame.math.Vector2(1, 1)
player_speed = 250

clock = pygame.time.Clock()
# Plain Surface
surf = pygame.Surface((200, 200))
surf.fill('orange')

# Importing an image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 300))

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_position = [(randint(0,1280),randint(0,720)) for i in range(20)]

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (0 + 20, WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    display_surface.fill('sky blue')

    for pos in star_position:
        display_surface.blit(star_surf, pos)

    player_rect.center += player_direction * player_speed * dt

    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0 :
        player_direction.x *= -1

    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0 :
        player_direction.y *= -1

    display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    pygame.display.update()
pygame.quit()