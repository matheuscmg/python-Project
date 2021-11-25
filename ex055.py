qtm = int(0)
pesoP = float(1000)
pesoM = float(0)
for i in range(1, 6):
    peso = (float(input(f'Digite o peso da {i}° pessoa:')))
    if peso > pesoM:
       pesoM = peso
    if peso < pesoP:
     pesoP = peso
print(f'Maior peso registrado: {pesoM} kg')
print(f'Menor peso registrado: {pesoP} kg')
