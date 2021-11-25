opc = str(input('Digite o seu sexo:')).strip().upper()
while opc not in 'MmFf':
    opc=input(f'Dado invalido informe novamente o seu sexo M/F:')
print(f'Sexo {opc} registrado com sucesso. ')