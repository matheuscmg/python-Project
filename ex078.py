valores = []
maior = 0
menor = 0
pos = []
posp = []
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a pos {i+1}:')))
    if i == 0:
        maior = valores[i]
        menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
            pos.append(i)
        if valores[i] < menor:
            menor = valores[i]
            posp.append(i)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor foi o {maior} e a posição dele foi {pos}')
print(f'O menor valor foi o {menor} e a posição dele foi {posp}')

'''outro modo de se fazer
print(f"Você digitou os valores: {valores}")
print(f"O menor valor digitado foi o {min(valores)} na posição {valores.index(min(valores))}.")
print(f"O maior valor digitado foi o {max(valores)} na posição {valores.index(max(valores))}.")'''
