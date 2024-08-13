from configuracao import *

class Main:
    def __init__(self):
        # geral
        pygame.init()
        self.display_surface = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()
