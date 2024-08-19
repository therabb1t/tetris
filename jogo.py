from configuracao import *

class Jogo:
    def __init__(self):
        self.surface = pygame.Surface((LARGURA_JOGO, ALTURA_JOGO))
        self.display_surface = pygame.display.get_surface()
    def run(self):
        self.display_surface.blit(self.surface, (PADDING,PADDING)) #block image transfer, ou seja, vai colocar uma superficie acima de outra.