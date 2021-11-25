dado = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in dado:
        dado.append(n)
        print('Valor adicionado')
    else:
        print('Valor ja digitado.')
    opc = int(input('Digite 1 para continuar e 999 para sair:'))
    print('*-'*25)
    if opc == 999:
        break
dado.sort()
print(f'Os valores ordanados são {dado}')
