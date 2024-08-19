from configuracao import *
from sys import exit

# componentes
from jogo import Jogo
from pontuacao import Pontuacao

class Main:
    # abre a janela do tetris
    def __init__(self):
        # geral
        pygame.init()
        self.display_surface = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA)) # define a janela
        self.clock = pygame.time.Clock() #define os frames do jogo
        pygame.display.set_caption('Tetris') # define o nome do jogo
        # componentes
        self.jogo = Jogo()
        self.pontuacao = Pontuacao()

    # fecha a janela do tetris
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill(CINZA) # cor do fundo
            # componentes
            self.jogo.run()
            self.pontuacao.run()
            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()
