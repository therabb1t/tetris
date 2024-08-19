from configuracao import *

class Pontuacao:
    def __init__(self):
        self.surface = pygame.Surface((LARGURA_LADO,ALTURA_JOGO*ALTURA_PONTUACAO-PADDING)) # define a altura e largura da sidebar
        self.rect =  self.surface.get_rect() #awquiiii eu parei aquiiiiii olah euuuuu
        self.display_surface = pygame.display.get_surface()
    def run(self):
        self.display_surface.blit(self.surface,(0,0))