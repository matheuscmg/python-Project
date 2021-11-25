from random import randint
num=(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
menor=15**15
maior=0
print(num)
for i in range(0,5):
    if num[i] > maior:
        maior=num[i]
    if num[i] < menor:
        menor =num[i]
print(f'Maior numero {maior}')
print(f'Menor numero {menor}')
