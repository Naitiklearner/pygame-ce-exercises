import pygame
from settings import *
from os.path import join

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class AnimatedSprite(Sprite):
    def __init__(self, frames, pos, groups):
        self.frames = frames
        self.frame_index = 0
        self.frame_speed = 10
        super().__init__(pos, self.frames[self.frame_index], groups)

    def animate(self, dt):
        self.frame_index += self.frame_speed * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

class Player(AnimatedSprite):

    def __init__(self, pos, groups, collision_sprites, frames):
        super().__init__(frames, pos, groups)
        self.flip = False

        self.direction = pygame.Vector2(0, 0)
        self.speed =  500
        self.collision_sprites = collision_sprites
        self.gravity = 90

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        if keys[pygame.K_SPACE] and self.on_floor: self.jump()

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
        
    def animate(self, dt):
        if self.direction.x:
            self.frame_index += self.frame_speed * dt
            self.flip = self.direction.x < 0
        else:
            self.frame_index = 0

        self.frame_index = 1 if not self.on_floor else self.frame_index

        self.image = self.frames[int(self.frame_index) % len(self.frames)]
        self.image = pygame.transform.flip(self.image, self.flip, False)

    def collision(self, direction):
        pass
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
    def check_floor(self):
        bottom_rect = pygame.FRect((0, 0), (self.rect.width, 2)).move_to(midtop = self.rect.midbottom)
        level_rects = [sprite.rect for sprite in self.collision_sprites]
        self.on_floor = True if bottom_rect.collidelist(level_rects) >= 0 else False

    def update(self, dt):
        self.check_floor()
        self.input()
        self.animate(dt)
        self.move(dt)
        self.collision(None)

class Bee(AnimatedSprite):
    def __init__(self, pos, groups, frames):
        super().__init__(frames, pos, groups)
    
    def update(self, dt):
        self.animate(dt)

class Worm(AnimatedSprite):
    def __init__(self, pos, groups, frames):
        super().__init__(frames, pos, groups)
    
    def update(self, dt):
        self.animate(dt)