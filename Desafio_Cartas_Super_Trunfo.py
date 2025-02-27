import random

# Definindo as cartas (poderia ser mais complexo, com mais atributos)
class Carta:
    def __init__(self, nome, forca, defesa, velocidade):
        self.nome = nome
        self.forca = forca
        self.defesa = defesa
        self.velocidade = velocidade

    def __str__(self):
        return f'{self.nome} - Força: {self.forca}, Defesa: {self.defesa}, Velocidade: {self.velocidade}'

# Lista de cartas
cartas = [
    Carta("Super-Herói 1", 80, 70, 90),
    Carta("Super-Herói 2", 85, 60, 95),
    Carta("Vilão 1", 75, 85, 60),
    Carta("Vilão 2", 90, 65, 80),
    Carta("Herói 3", 70, 75, 85)
]

# Função para comparar as cartas
def comparar_cartas(carta_jogador, carta_oponente, atributo):
    if getattr(carta_jogador, atributo) > getattr(carta_oponente, atributo):
        return "Você venceu!"
    elif getattr(carta_jogador, atributo) < getattr(carta_oponente, atributo):
        return "Oponente venceu!"
    else:
        return "Empate!"

# Função para jogar o Super Trunfo
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

# Função principal
if __name__ == "__main__":
    print("Bem-vindo ao Super Trunfo!")
    jogar_super_trunfo()