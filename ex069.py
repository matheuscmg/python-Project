qtdm = 0
qtdf = 0
maior=0
while True:
    print('*-'*10)
    idade = int(input('\nDigite a idade:'))
    sexo = str(input('Digite o sexo [m/f]')).upper()
    if sexo == 'M': qtdm += 1
    if sexo == 'F' and idade < 20: qtdf += 1
    if idade > 18 :maior+=1
    opc=str(input('Deseja continuar [S/N]:')).upper()
    if opc =='N': break
print(f'A quantidade de pessoas maiores de 18: {maior}')
print(f'A quantidade de homens cadastrados é de: {qtdm}')
print(f'A quantidade de mulheres com menos de 20 anos: {qtdf}')

