from random import randint
while True:
    print('''    Jogo de impar e par
    1-impar
    2-par  ''')

    opc=int(input('O que deseja ser impar ou par:'))
    n = int(input('Digite a sua um numero de 1 - 10:'))
    if opc >2 or opc<0 or 1 > n >10:
        print ('Opção invalida')
        break
    pc=randint(1,10)
    print(pc)
    if opc == 2 and (n+pc%2)==0:
        print('-Você ganhou-' * 10)
    elif opc ==1 and (n+pc%2)!=0:
        print('-Você ganhou-' * 10)
    else:
        print ('O Computador Ganhou')
        break




