import pygame.mixer

from configuracao import *
from sys import exit

# componentes
from jogo import Jogo
from pontuacao import Pontuacao
from pecas import Pecas
from random import choice

class Main:
    # abre a janela do tetris
    def __init__(self):
        # geral
        pygame.init()
        self.display_surface = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA)) # define a janela
        self.clock = pygame.time.Clock() #define os frames do jogo
        pygame.display.set_caption('Tetris') # define o nome do jogo
        #formatos
        self.proximos_formatos = [choice(list(TETROMINOS.keys())) for shape in range(3)]
        # componentes
        self.jogo = Jogo(self.adquirir_proximo_formato, self.atualizacao_pontos)
        self.pontuacao = Pontuacao()
        self.pecas = Pecas()
    def atualizacao_pontos(self, lines, score, level):
        self.pontuacao.lines = lines
        self.pontuacao.score = score
        self.pontuacao.level = level
    def adquirir_proximo_formato(self):
        proximo_formato = self.proximos_formatos.pop(0)
        self.proximos_formatos.append(choice(list(TETROMINOS.keys())))
        return proximo_formato

    # fecha a janela do tetris
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill(CINZA) # cor do fundo
            #componentes
            self.jogo.loop()
            self.pontuacao.loop()
            self.pecas.loop(self.proximos_formatos)
            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.loop()
