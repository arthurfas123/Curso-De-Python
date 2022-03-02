def area(a, b):
    n = a * b
    print('=-=' * 15)
    print(f'Area do terreno: {n}m.')


print('Calculando area!!!')
print('=-=' * 15)
l = float(input('Largura [m]: '))
c = float(input('Comprimento [m]: '))
area(l, c)
