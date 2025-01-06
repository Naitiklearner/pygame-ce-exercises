
from settings import * 
from sprites import * 
from groups import AllSprites
import json

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.running = True
    
        # sprites 
        self.all_sprites = AllSprites()
        self.paddle_sprites = pygame.sprite.Group()
        self.ball_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites, self.paddle_sprites))

        self.ball_spawn = True

        self.ball_event = pygame.event.custom_type()
        pygame.time.set_timer(self.ball_event, 5000)
        self.ball_timer = pygame.time.get_ticks()
        try:
            with open(join('data', 'score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {'player' : 0, 'opponent' : 0}
        self.font = pygame.font.Font(join('ARCADE_N.TTF'), 50)

    def ball_spawn_time(self):
        text_surf = self.font.render(str(self.ball_timer), True, (COLORS['bg detail']))
        text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH/2, 290))
        if self.ball_timer < 5.001:
            self.display_surface.blit(text_surf, text_rect)

    def display_score(self):
        player_surf = self.font.render(str(self.score['player']), True, (COLORS['bg detail']))
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2 + 100, 200))
        # if self.ball_timer < 5.001:
        self.display_surface.blit(player_surf, player_rect)

        opponent_surf = self.font.render(str(self.score['opponent']), True, (COLORS['bg detail']))
        opponent_rect = opponent_surf.get_frect(center = (WINDOW_WIDTH/2 - 100, 200))
        self.display_surface.blit(opponent_surf, opponent_rect)

        pygame.draw.line(self.display_surface, COLORS['bg detail'], ( WINDOW_WIDTH /2, 0),(WINDOW_WIDTH /2, WINDOW_HEIGHT), 6)
    
    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('data', 'score.txt'), 'w') as score_file:
                        json.dump(self.score, score_file)
                if event.type == self.ball_event and self.ball_spawn:
                    self.ball = Ball((self.all_sprites, self.ball_sprites), self.paddle_sprites,  self.update_score)
                    self.opponent = Opponent((self.all_sprites, self.paddle_sprites), self.ball)
                    self.ball_spawn = False
            # update

            self.all_sprites.update(dt)

            # draw 
            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.ball_spawn_time()
            self.all_sprites.draw()

            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()