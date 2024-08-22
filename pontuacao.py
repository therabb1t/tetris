from configuracao import *
from os.path import join

class Pontuacao:
    def __init__(self):
        self.surface = pygame.Surface((LARGURA_LADO,ALTURA_JOGO*ALTURA_PONTUACAO-PADDING)) # define a altura e largura da sidebar
        self.rect =  self.surface.get_rect(bottomright = (LARGURA_JANELA - PADDING,ALTURA_JANELA - PADDING)) #joga a sidebar para o canto inferior direito
        self.display_surface = pygame.display.get_surface()

        #fonte
        self.font = pygame.font.Font(join('graphics','Russo_One.ttf'), 20)
        #encremento
        self.increment_height = self.surface.get_height() / 3
        #dados
        self.score = 0
        self.level = 1
        self.lines = 0
    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, 'white')
        text_rext = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface,text_rext)
    def loop(self):
        self.surface.fill(CINZA)
        for i, text in enumerate([('Pontos',self.score),('Nível',self.level),('Linhas', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x,y),text)
        self.display_surface.blit(self.surface,self.rect)
        pygame.draw.rect(self.display_surface, COR_LINHA, self.rect, 2, 2)