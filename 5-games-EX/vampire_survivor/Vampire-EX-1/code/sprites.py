from settings import *

class CollisionSprites(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.Surface(size)
        self.image.fill('blue')
        self.rect = self.image.get_frect(center = pos)