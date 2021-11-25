while True:
    valor = float(input('Qual valor você deseja sacar:'))
    if valor > 50:
        nota50 = valor // 50
        valor = valor - (nota50 * 50)
        print(f'Total de {nota50} cedulas de 50$ ')
    if valor >= 20:
        nota20 = valor // 20
        valor = valor - (nota20 * 20)
        print(f'Total de {nota20} cedulas de 20$ ')
    if valor >= 10:
        nota10 = valor // 10
        valor = valor - (nota10 * 10)
        print(f'Total de {nota10} cedulas de 10$ ')
    if valor >= 1:
        nota1 = valor // 1
        valor = valor - (nota1 * 1)
        print(f'Total de {nota1} cedulas de 1$ ')
    break




