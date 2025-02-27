<H1>Desafio de Carta Super Trunfo</H1>

<p>Descrição Detalhada do Código
Este código implementa uma versão simples de um jogo de Super Trunfo com cartas que possuem atributos como força, 
defesa e velocidade. O jogador e o oponente comparam as cartas baseadas em um desses atributos para determinar 
o vencedor da rodada.

Vamos detalhar o funcionamento do código:

1. Definição da Classe Carta
A primeira parte do código define a classe Carta, que representa as cartas do jogo. Cada carta tem 4 atributos:

nome: O nome da carta (por exemplo, "Super-Herói 1").
forca: A força do personagem na carta.
defesa: A defesa do personagem na carta.
velocidade: A velocidade do personagem na carta.
Método __init__: O construtor da classe recebe o nome, força, defesa e velocidade, e os atribui aos atributos da carta.

Método __str__: Este método retorna uma string formatada representando a carta, incluindo os valores de força, 
defesa e velocidade. Ele é utilizado quando você imprime uma instância da classe Carta, facilitando a exibição 
das informações da carta.

python
Copiar
class Carta:
    def __init__(self, nome, forca, defesa, velocidade):
        self.nome = nome
        self.forca = forca
        self.defesa = defesa
        self.velocidade = velocidade

    def __str__(self):
        return f'{self.nome} - Força: {self.forca}, Defesa: {self.defesa}, Velocidade: {self.velocidade}'
2. Lista de Cartas
Em seguida, o código cria uma lista chamada cartas, que contém várias instâncias da classe Carta.
Cada carta representa um personagem com valores específicos de força, defesa e velocidade.

Exemplo de cartas incluídas:

Super-Herói 1 com força 80, defesa 70, e velocidade 90.
Vilão 1 com força 75, defesa 85, e velocidade 60.
python
Copiar
cartas = [
    Carta("Super-Herói 1", 80, 70, 90),
    Carta("Super-Herói 2", 85, 60, 95),
    Carta("Vilão 1", 75, 85, 60),
    Carta("Vilão 2", 90, 65, 80),
    Carta("Herói 3", 70, 75, 85)
]
3. Função comparar_cartas
A função comparar_cartas recebe duas cartas e um atributo (por exemplo, "forca", "defesa", ou "velocidade"). 
Ela compara os valores do atributo escolhido nas cartas e retorna o resultado da comparação:

Se o atributo da carta do jogador for maior, ele vence a rodada.
Se o atributo da carta do oponente for maior, o oponente vence.
Se ambos os atributos forem iguais, o resultado é empate.
Para acessar o atributo de uma carta de forma dinâmica, a função usa getattr(), que permite acessar 
o atributo de uma instância de classe usando o nome do atributo como string.

python
Copiar
def comparar_cartas(carta_jogador, carta_oponente, atributo):
    if getattr(carta_jogador, atributo) > getattr(carta_oponente, atributo):
        return "Você venceu!"
    elif getattr(carta_jogador, atributo) < getattr(carta_oponente, atributo):
        return "Oponente venceu!"
    else:
        return "Empate!"
4. Função jogar_super_trunfo
A função jogar_super_trunfo é responsável por simular uma rodada do jogo. Ela faz o seguinte:

Embaralha as cartas com random.shuffle(cartas).
Escolhe as duas primeiras cartas da lista como as cartas do jogador e do oponente.
Exibe as cartas do jogador e do oponente no console.
Solicita ao jogador a escolha de um atributo para a comparação (força, defesa ou velocidade).
Valida a escolha do atributo, garantindo que o jogador tenha escolhido uma opção válida.
Compara as cartas usando a função comparar_cartas e imprime o resultado da rodada.
python
Copiar
def jogar_super_trunfo():
    random.shuffle(cartas)
    carta_jogador = cartas[0]
    carta_oponente = cartas[1]

    print("Sua carta: ")
    print(carta_jogador)
    print("\nCarta do Oponente: ")
    print(carta_oponente)

    # O jogador escolhe o atributo para comparar
    atributo = input("\nEscolha um atributo para comparar (forca, defesa, velocidade): ").strip().lower()

    # Validando a escolha do atributo
    if atributo not in ['forca', 'defesa', 'velocidade']:
        print("Atributo inválido!")
        return

    # Comparando as cartas
    resultado = comparar_cartas(carta_jogador, carta_oponente, atributo)
    print(resultado)
    
5. Função Principal
A função principal (if __name__ == "__main__":) é responsável por iniciar o jogo. Ela exibe uma mensagem
de boas-vindas e chama a função jogar_super_trunfo() para começar o jogo.

python
Copiar
if __name__ == "__main__":
    print("Bem-vindo ao Super Trunfo!")
    jogar_super_trunfo()
Resumo do Jogo
Objetivo: O jogador escolhe um atributo para comparar com oponente e ganha a rodada se o valor desse atributo for maior.
Cartas: Cada carta tem atributos de força, defesa e velocidade, e o jogador pode escolher qualquer um desses atributos
para comparar na rodada.
Interatividade: O jogador escolhe qual atributo usar na comparação e o resultado (vitória, derrota ou empate) é 
mostrado após a comparação.
Este código é um exemplo simples, mas pode ser expandido para adicionar mais funcionalidades, como várias rodadas, 
mais cartas, e até uma interface gráfica ou uma versão multiplayer.</p>
