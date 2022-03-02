print('=-=' * 18)
print(' ' * 10, 'TABELA DE PREÇOS')
print('=-=' * 18)
produtos = ('Lápis', 1.50,
            'Caneta', 1.00,
            'Caderno', 5.80,
            'Bolacha', 1.75,
            'Bolo', 1.25)
cont = 0
print('PRODUTOS', ' ' * 36, 'VALOR')
print('=-=' * 18)
for c in produtos:
    if cont % 2 == 0:
        print(f'{c:.<40}', end='')
    if cont % 2 != 0:
        print(f'R${c:>9.2f}')
    cont += 1
