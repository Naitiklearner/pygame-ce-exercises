from settings import * 

class Timer:
    def __init__(self, duration, func = None, repeat = None, autostart = False):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.timer = 0
        self.active = False
        self.repeat = repeat
        
        if autostart:
            self.activate()

    def __bool__(self):
        return self.active
    
    def activate(self):
        self.start_time = pygame.time.get_ticks()
        self.active = True

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()
        else:
            self.active = False

        
    def update(self):
        if pygame.time.get_ticks() - self.start_time >= self.duration:
            if  self.func and self.start_time != 0:
                self.func()
            self.deactivate()
