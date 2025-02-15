from settings import * 

class Player(pygame.sprite.Sprite):
        def __init__(self, pos, groups):
            super().__init__(groups)    
            self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
            self.rect = self.image.get_frect(center = pos)
            self.direction = pygame.math.Vector2()
            self.speed = 200
        
        def input(self):
            keys = pygame.key.get_pressed()
            self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
            self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        
        def move(self, dt):
            self.direction.normalize() if self.direction else self.direction
            self.rect.center += self.direction * self.speed * dt

        def update(self, dt):
            self.input()
            self.move(dt)
