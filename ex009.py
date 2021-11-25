valor = float(input('Digite o valor do produto:'))
desc = float(input('Digite a porcentagem de desconto:'))
res =(valor*(desc/100))

print ('o valor do produto com desconto é de : {}'.format(valor-res))