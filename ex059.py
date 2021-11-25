n1=float(input('Digite o primeiro valor:'))
n2=float(input('Digite o segundo valor:'))
opc=int(0)
while opc != 5:
    print('[1] Somar os numeros')
    print('[2] Multiplicar os numeros')
    print('[3] Maior numero')
    print('[4] Novos numeros')
    print('[5] Para sair do programa')
    opc=input('Digite a sua opção:')
    if opc == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif opc == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif opc == 3:
        if n1 > n2:
            print(f'O maior numero é o {n1}')
        else:
            print(f'O maior numero é o {n2}')
    elif opc == 4:
        n2 = input('Digite o segundo valor:')
        n1 = input('Digite o primeiro valor:')






