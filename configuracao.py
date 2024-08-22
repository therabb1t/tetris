import pygame

# tamanho do jogo
COLUNAS = 10
LINHAS = 20
CELULA = 30
LARGURA_JOGO, ALTURA_JOGO = COLUNAS * CELULA, LINHAS * CELULA

# tamanho do display ao lado
LARGURA_LADO = 160
ALTURA_PECAS = 0.7
ALTURA_PONTUACAO = 1 - ALTURA_PECAS

# janela
PADDING = 15
LARGURA_JANELA = LARGURA_JOGO + LARGURA_LADO + PADDING * 3
ALTURA_JANELA = ALTURA_JOGO + PADDING * 2

#comportamento
ATUALIZACAO_VELOCIADE_INCIAL = 600
ESPERA_MOVIMENTO = 200
ESPERA_ROTACAO = 200
DESVIO_BLOCO = pygame.Vector2(COLUNAS // 2, -1)

# cores!!
CIANO = '#0EE3E7'
AZUL = '#1208D6'
VERDE = '#27FF00'
AMARELO = '#FFDD20'
LARANJA = '#FF5D00'
VERMELHO = '#cf0030'
ROXO = '#9C00FB'
CINZA = '#1B1B1B'
COR_LINHA = '#ffffff'

# formatos
TETROMINOS = {
    'T':{'formato':[(0,0), (-1,0), (1,0), (0,-1)], 'cor': ROXO},
    'O':{'formato':[(0,0), (0,-1), (1,0), (1,-1)], 'cor': AMARELO},
    'j':{'formato':[(0,0), (0,-1), (0,1), (-1,1)], 'cor': AZUL},
    'L':{'formato':[(0,0), (0,-1), (0,1), (1,1)], 'cor': LARANJA},
    'I':{'formato':[(0,0), (0,-1), (0,-2), (0,1)], 'cor': CIANO},
    'S':{'formato':[(0,0), (-1,0), (0,-1), (1,-1)], 'cor': VERDE},
    'Z':{'formato':[(0,0), (1,0), (0,-1), (-1,-1)], 'cor': VERMELHO},
}
DADOS_PONTUACAO = {1: 40, 2: 100, 3: 300, 4: 1200}