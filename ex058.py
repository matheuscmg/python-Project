from random import randint
qtd = 1
pc = randint(0, 10)
jogador = int(input('Vou pensar em um número de 0 a 10, Tente advinhar: '))
while jogador != pc:
    jogador = int(input('Você errou, tente novamente: '))
    qtd += 1
print(f'Parabéns, você ganhou em {qtd} tentativas!')