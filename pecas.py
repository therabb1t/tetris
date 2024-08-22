from configuracao import *
from pygame.image import load
from os import path

class Pecas:
    def __init__(self):
        #geral
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((LARGURA_LADO, ALTURA_JOGO * ALTURA_PECAS))
        self.rect = self.surface.get_rect(topright = (LARGURA_JANELA - PADDING, PADDING))
        #formatos
        self.shape_surfaces = {shape: load(path.join('graphics', f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}
        self.increment_height = self.surface.get_height() / 3

    def display_pieces(self, shapes):
        for i, formato in enumerate(shapes):
            shape_surface = self.shape_surfaces[formato]
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            rect = shape_surface.get_rect(center=(x, y))
            self.surface.blit(shape_surface, rect)

    def loop(self, proximo_formato):
        self.surface.fill(CINZA)
        self.display_pieces(proximo_formato)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, COR_LINHA, self.rect, 2, 2)
