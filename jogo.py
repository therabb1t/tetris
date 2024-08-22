import pygame.sprite

from configuracao import *
from random import choice
from timer import Timer

class Jogo:
    def __init__(self, adquirir_proximo_formato, atualizacao_pontos):
        #geral
        self.surface = pygame.Surface((LARGURA_JOGO, ALTURA_JOGO))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        #conexão de jogo
        self.adquirir_proximo_formato = adquirir_proximo_formato
        self.atualizacao_pontos = atualizacao_pontos

        #linhas
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((0,255,0))

        #tetrominó
        self.dados_area = [[0 for x in range(COLUNAS)] for y in range(LINHAS)]
        self.tetromino = Tetromino(
            choice(list(TETROMINOS.keys())),
            self.sprites,
            self.criar_novo_tetromino,
            self.dados_area)

        #timer
        self.velocidade_baixo = ATUALIZACAO_VELOCIADE_INCIAL
        self.velocidade_baixo_maior = self.velocidade_baixo * 0.3
        self.baixo_pressionado = False
        self.timers = {
            'movimento vertical': Timer(ATUALIZACAO_VELOCIADE_INCIAL, True, self.mover_baixo),
            'movimento horizontal': Timer(ESPERA_MOVIMENTO),
            'rotacionar': Timer(ESPERA_ROTACAO)
        }
        self.timers['movimento vertical'].ativar()

        #portuação
        self.nivel_atual = 1
        self.pontuacao_atual = 0
        self.linha_atual = 0

    def calcula_pontos(self, n_linhas):
        self.linha_atual += n_linhas
        self.pontuacao_atual += DADOS_PONTUACAO[n_linhas] * self.nivel_atual

        if self.linha_atual / 10 > self.nivel_atual:
            self.nivel_atual += 1
        self.atualizacao_pontos(self.linha_atual, self.pontuacao_atual, self.nivel_atual)

    def criar_novo_tetromino(self):

        self.checar_linhas_completas()
        self.tetromino = Tetromino(
            self.adquirir_proximo_formato(),
            self.sprites,
            self.criar_novo_tetromino,
            self.dados_area)
    def atualizacao_timer(self):
        for timer in self.timers.values():
            timer.atualizacao()
    def mover_baixo(self):
        self.tetromino.mover_baixo()
    def grade(self): #cria uma grid
        for col in range(1, COLUNAS): #linhas verticais
            x = col * CELULA
            pygame.draw.line(self.surface, COR_LINHA, (x,0), (x,self.surface.get_height()), 1)

        for lin in range(1, LINHAS): #linhas horizontais
            y = lin * CELULA
            pygame.draw.line(self.surface, COR_LINHA, (0,y), (self.surface.get_width(),y))

        self.surface.blit(self.line_surface, (0,0))
    def input(self): #movimenta os blocos da direita para esquerda (vise-versa)
        keys = pygame.key.get_pressed()

        #checando o movimento horizontal
        if not self.timers['movimento horizontal'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.mover_horizontal(-1)
                self.timers['movimento horizontal'].ativar()
            if keys[pygame.K_RIGHT]:
                self.tetromino.mover_horizontal(1)
                self.timers['movimento horizontal'].ativar()
        #checando a rotação
        if not self.timers['rotacionar'].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotacionar()
                self.timers['rotacionar'].ativar()

        #aumento na velocidade para baixo
        if not self.baixo_pressionado and keys[pygame.K_DOWN]:
            self.baixo_pressionado = True
            self.timers['movimento vertical'].duration = self.velocidade_baixo_maior
        if self.baixo_pressionado and not keys[pygame.K_DOWN]:
            self.baixo_pressionado = False
            self.timers['movimento vertical'].duration = self.velocidade_baixo

    def checar_linhas_completas(self):
        #pegar o índice das linhas cheias
        deletar_linhas = []
        for i, lin in enumerate(self.dados_area):
            if all(lin):
                deletar_linhas.append(i)
        if deletar_linhas:
            for deletar_linha in deletar_linhas:
                #deleta linhas cheias
                for bloco in self.dados_area[deletar_linha]:
                    bloco.kill()
                #move os blocos para baixo
                for lin in self.dados_area:
                    for bloco in lin:
                        if bloco and bloco.pos.y < deletar_linha:
                            bloco.pos.y += 1
            #reconstruir os dados da area
            self.dados_area = [[0 for x in range(COLUNAS)] for y in range(LINHAS)]
            for bloco in self.sprites:
                self.dados_area[int(bloco.pos.y)][int(bloco.pos.x)] = bloco
            #atualização de pontos
            self.calcula_pontos(len(deletar_linhas))
    def loop(self):
        #atualização
        self.input()
        self.atualizacao_timer()
        self.sprites.update()

        #desenhar
        self.surface.fill(CINZA)
        self.sprites.draw(self.surface)

        self.grade()
        self.display_surface.blit(self.surface, (PADDING,PADDING)) #block image transfer, ou seja, vai colocar uma superficie acima de outra.
        pygame.draw.rect(self.display_surface, COR_LINHA, self.rect, 2, 2)

class Tetromino:
    def __init__(self, shape, group, criar_novo_tetromino, dados_area):
        #setup
        self.shape =  shape
        self.block_positions = TETROMINOS[shape]['formato']
        self.color = TETROMINOS[shape]['cor']
        self.criar_novo_tetromino = criar_novo_tetromino
        self.dados_area = dados_area

        #blocos
        self.blocks = [Bloco(group, pos, self.color) for pos in self.block_positions]

    #colisão
    def colisao_proximo_movimento_horizontal(self, blocks, amount): #colisão nas paredes
        lista_colisao = [bloco.colisao_horizontal(int(bloco.pos.x + amount), self.dados_area) for bloco in self.blocks]
        return True if any(lista_colisao) else False
    def colisao_proximo_movimento_vertical(self, blocks, amount): #colisão no chão
        lista_colisao = [bloco.colisao_vertical(int(bloco.pos.y + amount), self.dados_area) for bloco in self.blocks]
        return True if any(lista_colisao) else False

    #movimentos
    def mover_horizontal(self, amount):
        if not self.colisao_proximo_movimento_horizontal(self.blocks, amount):
            for bloco in self.blocks:
                bloco.pos.x += amount
    def mover_baixo(self):
        if not self.colisao_proximo_movimento_vertical(self.blocks, 1):
            for bloco in self.blocks:
                bloco.pos.y += 1
        else:
            for bloco in self.blocks:
                self.dados_area[int(bloco.pos.y)][int(bloco.pos.x)] = bloco
            self.criar_novo_tetromino()

    #rotação
    def rotacionar(self):
        if self.shape != 'O':
            #1. âncora de rotação
            pos_ancora = self.blocks[0].pos

            #2. nova posição dos blocos
            nova_pos_bloco = [bloco.rotacionar(pos_ancora) for bloco in self.blocks]

            #3. checando a colisão
            for pos in nova_pos_bloco:
                #horizontal / paredes
                if pos.x < 0 or pos.x >= COLUNAS:
                    return
                #area / outras peças
                if self.dados_area[int(pos.y)][int(pos.x)]:
                    return
                #vertical / chão
                if pos.y > LINHAS:
                    return

            #4. implementar novas posições
            for i, bloco in enumerate(self.blocks):
                bloco.pos = nova_pos_bloco[i]


class Bloco(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        #geral
        super().__init__(group)
        self.image = pygame.Surface((CELULA,CELULA))
        self.image.fill(color)

        #posição
        self.pos = pygame.Vector2(pos) + DESVIO_BLOCO
        self.rect = self.image.get_rect(topleft = self.pos * CELULA)
    def rotacionar(self, pos_ancora):
        return pos_ancora + (self.pos - pos_ancora).rotate(90)
    def colisao_horizontal(self, x, dados_area):
        if not 0 <= x < COLUNAS:
            return True
        if dados_area[int(self.pos.y)][x]:
            return True
    def colisao_vertical(self, y, dados_area):
        if y >= LINHAS:
            return True
        if y >= 0 and dados_area[y][int(self.pos.x)]:
            return True
    def update(self):
        self.rect.topleft = self.pos * CELULA