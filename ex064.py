num = int(0)
qtd = int(0)
soma = int(0)
while num != 999:
    num = int(input('Digite um valor [999 para parar]:'))
    if num != 999:
        soma = soma + num
        qtd = qtd + 1
print(f'Quantidade de elementos {qtd} soma de {soma}')
