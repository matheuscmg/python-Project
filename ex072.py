numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove','Dez', 'Onze', 'Doze', 'Treze',
    'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um numero de 0-20:'))
if num <=20 and num >=0:
    for i in range (0,21):
        if(i==num):
            print(f'O numero que você digitou foi {numero[i]}')
else:
    print ('Numero invalido')