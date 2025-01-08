from settings import * 
from sprites import *
from groups import AllSprites
from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.enemies_sprites = pygame.sprite.Group()


        self.load_assets()
        self.setup()

        self.worm = Worm((200, 550), (self.all_sprites), self.worm_frames)
        self.bee = Bee((200, 600), (self.all_sprites), self.bee_frames)
    def load_assets(self):
        self.player_frames = import_folder('images', 'player')
        self.bullet_surf = import_image('images', 'gun', 'bullet')
        self.fire_surf = import_image('images', 'gun', 'fire')
        self.bee_frames = import_folder('images', 'enemies', 'bee')
        self.worm_frames = import_folder('images', 'enemies', 'worm')

        self.impact_sound = pygame.mixer.Sound(join('audio', 'impact.ogg'))
        self.game_music = pygame.mixer.Sound(join('audio', 'music.wav'))
        self.shoot_sound = pygame.mixer.Sound(join('audio', 'shoot.wav'))



    def setup(self):
        self.tmx_data = load_pygame(join('data', 'maps', 'world.tmx'))
        for x,y, image in self.tmx_data.get_layer_by_name('Main').tiles():
            Sprite((x * TILE_SIZE,y * TILE_SIZE), image, (self.all_sprites, self.collision_sprites))
        for x,y, image in self.tmx_data.get_layer_by_name('Decoration').tiles():
            Sprite((x * TILE_SIZE,y * TILE_SIZE), image, (self.all_sprites))
        for obj in self.tmx_data.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x, obj.y), (self.all_sprites), self.collision_sprites, self.player_frames)
            # if obj.name == 'Worm':

                # if layer.name == 'Main':
                #     for obj in layer:
                #         if obj.name == 'Main':
                            

    def run(self):
        while self.running:
            dt = self.clock.tick(FRAMERATE) / 1000 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
            

            # update
            self.all_sprites.update(dt)

            # draw 
            self.display_surface.fill(BG_COLOR)
            self.all_sprites.draw(self.player.rect.center)

            pygame.display.update()
        
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run() 