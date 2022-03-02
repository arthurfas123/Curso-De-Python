print('ALUGUEL DE CARROS!!!')
km = int(input('KM ANDADOS: '))
dias = int(input('DIAS ALUGADOS: '))
print(f'VALOR: {(dias * 60) + (km * 0.15):.2f}')
