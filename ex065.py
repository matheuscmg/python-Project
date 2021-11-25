num = maior = 0
menor = 15**15
qtd =0
soma =0
while num != 999:
    num = int(input('Digite um valor [999 para parar]:'))

    if num != 999:
        soma = soma + num
        qtd = qtd + 1
        if num>maior:
            maior=num
        if num < menor:
             menor =num

print(f'Quantidade de elementos {qtd} média é {soma/qtd}')
print(f'Maior numero digitado {maior} menor numero digitado {menor}')