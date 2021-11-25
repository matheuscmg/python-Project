first = int(input('Informe o 1 termo sequencia:'))
razao = int(input('Informe a razao'))
print(first)

for i in range(0, 9, ):
    first = first + razao
    print(f'{first}')

ans = 'a'
while ans != 'N':
    qtd = int(input('Você quer mostrar mais quantos termos?'))
    for i in range(0, qtd):
        first = first + razao
        print(f'{first}')
    ans = str(input('você quer mostrar mais termos?').upper())