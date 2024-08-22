# Tetris
Projeto em Python utilizando PyGame
>Apresentação


Tetris é um jogo simples que consiste em você encaixar peças até fechar uma linha, quanto mais linhas, mais pontos. 
Willis Gibson que foi o primeiro ser humano a zerar o tetris.
- Speedrun: tem como base a finalizar o jogo o mais rápido possível, normalmente como tetris é um jogo muito longo aqueles que praticam speedruns não o zeram, mas chegam a um determinado Level igual a 19 como no Tetris (NES-1988) que o campeão mundial até agora é o Cheez dos Estados Unidos.

O tetris inicialmente era um jogo de exercícios militares sovieticos para programas de inteligência artificial baseados em estratégia e matemática, criado por Alexey Pajitnov (Алексей Пажитнов) junto de seus colegas de trabalho Dmitry Pavlovsky e Vadim Gerasimov (Дмитрий Павловский и Вадим Герасимов) em um centro de pesquisa científica soviética, em 1984.

A linguagem de programação utilizada por Pajitnov foi **Pascal**, conhecido pela facilidade de orientação e criação de objetos, as peças e linhas do jogo eram feitos com pontos e colchetes. ( [ ] e . )

<p align="center">
  <img src="https://tetris.wiki/images/e/ea/Original_Tetris.png" width="400" height="300"/>
</p>

De 1984 á 1991 Alexey não ganhou absolutamente nada pela fama do seu jogo, o que envolvia uma polêmica entre o Governo Soviético com o empresário britânico Robert Stein que conseguiu cópias piratas do jogo, até enifm migrar para os EUA com Henk Rogers e fundarem a *The Tetris Company*.

<p align="center">
  <img src="https://forbes.com.br/wp-content/uploads/2023/04/Alexey-Pajitnov-793x533.jpg" width="400" height="300"/>
</p>

Após 40 anos de seu lançamento, mais de um bilhão de pessoas já jogaram tetris, o fênomeno da fama do jogo é explicado por Alexey Pajitnov a partir da lógica de: "o jogo lhe apresenta peças aletórias e fora de ordem, você é induzido á reordena-las e construir para sempre".


>Lista de funções e componentes que não conheciamos:
- `(self)`: É o primeiro argumento que passa por um construtor e ou nos métodos de instâncias (aquelas que importamos no inicio dos projetos), uma classe responsável por vincular atributos á outras funções ou métodos.
- `from os.path import join`: É um método de conectar componentes facilmente, inserindo o prefixo "/".

**Biblioteca PyGame:**

- `pygame.init`: inicia todos os módulos importados do pygame.

- `pygame.display`: controla a janela e tela do jogo.

- `pygame.time`: monitora o tempo.

- `pygame.event`: interage com eventos e listas.

- `pygame.mixer`: carrega e toca sons.

- `pygame.Surface`: representa imagens.

- `pygame.image`: carrega e salva imagens.

- `pygame.draw`: possibilita o uso de formas e desenhos.

- `pygame.quit`: desliga todos os módulos importados do pygame.

