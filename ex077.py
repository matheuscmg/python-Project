dado= ('Atletico-mg', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians',
        'internacional', 'Fluminense', 'Cuiabá', 'Athletico-PR')
alfa=('a','e','i','o','u')
for i in dado:
    print(f'\nA palavra {i} tem as vogais:', end=' ')
    for letra in i:
        if letra.lower() in alfa:
         print (letra, end=' ')
print('\nFim')
