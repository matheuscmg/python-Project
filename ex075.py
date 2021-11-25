num = (int(input('Digite um Valor:')),
       int(input('Digite um Valor:')),
       int(input('Digite um Valor:')),
       int(input('Digite um Valor:')))
qtd = 0
pos = 0
np=(0,1,2,3)
for i in range(0, len(num)):
    if num[i] == 9:
        qtd = qtd + 1
    if num[i] == 3:
        pos = i
print(f'Quantidade de numeros 9 foram {qtd}.')
print(f'Primeira posição de um numero 3 foi a posição {pos + 1}')
print('Os números pares foram :')
for i in range(0, len(num)):
    if num[i] % 2 == 0:
        print(num[i],end = ' ')

