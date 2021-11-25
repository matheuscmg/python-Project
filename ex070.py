total=0
qtd=0
menor=15**15
while True:
    print('-' * 25)
    prod=str(input('Digite o nome do produto:'))
    valor=float(input('Preço R$'))
    opc = str(input('Deseja continuar [S/N]:')).upper()
    total+=valor
    if valor > 1000:qtd+=1
    if valor < menor:
        menor = valor
        barato=prod
    if opc == 'N': break
print(f'O total da compra foi R${total}')
print(f'A quantidade de produtos custando mais quem 1000$ é :{qtd}')
print(f'O produto mais barato é {barato} e o valor é R${menor}')

