dados = ('Placa de video', 1799,
         'Memoria ram', 1599,
         'Processador', 2400,
         'Gabinete', 250)
for i in range(0, len(dados)):
    if i % 2 == 0:
        print(f'{dados[i]:.<25}', end=' ')
    else:
        print(f'R${dados[i]:>3}')
