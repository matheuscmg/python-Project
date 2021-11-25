qtdm=0
media=0
maior=0
homem=''
for i in range (1, 5):
    nome=str(input(f'Digite o {i}° nome:'))
    idade=int(input(f'Digite a idade da {i}° pessoa:'))
    sexo=str(input(f'Digite o sexo (M/F):'))
    media= media+idade
    if sexo=='f' and idade < 20:
        qtdm= qtdm+1
    if sexo=='m' and idade > maior:
        maior=idade
        homem= nome
print (f'A média das idades é {media/4}')
print(f'A quantidade de mulheres menores que 20 anos é:{qtdm}')
print(f'O homem mais velho é o {homem}')
