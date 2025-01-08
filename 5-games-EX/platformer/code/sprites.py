import pygame
from settings import *
from os.path import join

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.direction = pygame.Vector2(0, 0)
        self.speed =  500
        self.collision_sprites = collision_sprites
        self.gravity = 90
        self.on_floor = False
    def input(self):
        keys = pygame.key.get_pressed()
        keys_jump = pygame.key.get_just_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        if keys_jump[pygame.K_SPACE] and self.on_floor: self.jump()

    
    def jump(self):
        
        self.direction.y = -25
        self.direction.y += 1
    def move(self, dt):
        self.rect.centerx += self.direction.x * self.speed * dt
        self.collision('horizontal')

        self.on_floor = False
        self.direction.y += self.gravity * dt
        self.rect.centery += self.direction.y
        self.collision('vertical')
        

    def collision(self, direction):
        pass
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    if self.direction.y > 0: 
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                        self.on_floor = True
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
    def update(self, dt):
        self.input()
        self.move(dt)
        self.collision(None)

