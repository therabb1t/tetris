import pygame.time


class Timer:
    def __init__(self, duration, repeated = False, func = None):
        self.repeated = repeated
        self.func = func
        self.duration = duration

        self.start_time = 0
        self.active = False
    def ativar(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()
    def desativar(self):
        self.active =  False
        self.start_time = 0
    def atualizacao(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >=  self.duration and self.active:

            #chamar uma função
            if self.func and self.start_time != 0:
                self.func()

            #reseta o timer
            self.desativar()

            #repete o timer
            if self.repeated:
                self.ativar()
