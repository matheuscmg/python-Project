'''valor=list()
n=0
for c in range(0,5):
    valores=int(input('Digite um valor:'))
valor2= valor[:]
for i in range(0,5):
    for j in range(0,5):
        if valor[i] >valor2[j]:
            n= valor[i]
            valor[i] = valor2[j]
            valor[j]=n
print(valor)'''
import statistics

lista = [20, 20, 20, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23,
         23, 24, 24, 24, 24, 25, 25, 25, 25, 26]

for i in range(1, len(lista)):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave

print(f'A media é {statistics.mean(lista)}')
print(f'A mediana é {statistics.median(lista)}')
print(f'não sei {statistics.quantiles(lista)}')
print(f'O Desvio padrao {statistics.pstdev(lista)}')
print(f'A variancia é {statistics.variance(lista)}')


