time = ('Atletico-mg', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians',
        'internacional', 'Fluminense', 'Cuiabá', 'Athletico-PR')

print('-' * 20)
print('Os 5 primeior times são:')
for i in range(0, 5):
    print(time[i], end=' ')
print('\n', '-' * 20)

print('Os ultimos 4 times são:')
for i in range(6, 10):
    print(time[i], end=' ')
print('\n', '-' * 20)

print('Os Times em ordem Alfabeica são:')
time2 = sorted(time)
for i in range(0, len(time2)):
    print(time2[i], end=' ')

print('\n', '-' * 20)
for i in range(0, len(time)):
    if time[i] == 'Fluminense':
        print(f'A Posição do time Fluminense é {i}')
