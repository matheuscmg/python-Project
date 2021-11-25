num = int(input('Quantos termos de fibonnace deseja printar:'))
t1 = 0
t2 = 1
i = 3

while i <= num:
    if i==3:print(t1,t2, end= ' ')
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    i = i + 1
print('\nFim Da Sequência')
