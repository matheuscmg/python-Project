n= int (input('Digite um valor:'))

print('\n O dobro de {} é:{}'.format(n,n*2))
print('\n O triplo de {} é:{}'.format(n,n*3))
#print('\n A raiz quadrada de {} é:{} '.format(n,(n**(1/2))))
print('\n A raiz quadrada de {} é:{:.2f} '.format(n,pow(n,(1/2))))
#{:.2f} serve para limitar casas decimais
