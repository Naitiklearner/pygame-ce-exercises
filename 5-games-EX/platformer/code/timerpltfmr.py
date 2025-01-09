from settings import * 

class Timer:
    def __init__(self, duration, func = None, repeat = None, autostart = False):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.timer = 0
        self.active = False
        self.repeat = repeat
        
    def activate(self):
        self.start_time = pygame.time.get_ticks()
        self.active = True

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        if pygame.time.get_ticks() - self.start_time >= self.duration:
            if  self.func and self.start_time != 0:
                self.func()
            self.deactivate()
            # if self.repeat:
            #     self.start_time = pygame.time.get_ticks()
            # else:
            #     self.active = False