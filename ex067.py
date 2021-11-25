while True:
    n = int(input('Digite um numero para a tabuada:'))
    if n<0:break
    for i in range (1,11):
        print(f'{n} x {i} = {n * i}')
print('-fim-'*20)



