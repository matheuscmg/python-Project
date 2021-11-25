from datetime import date

qtdM = 0
qtdP = 0

for i in range(1, 7):
    ano=int(input(f'Digite o  ano de nascimento da {i}° pessoa:'))
    if (date.today().year) - (ano) > 21:
        qtdM += +1
    else:
        qtdP -= -1

print(f'Total de pessoas maiores de 21 anos de idade:{qtdM}')
print(f'Total de pessoas menores de 21 anos de idade:{qtdP}')
