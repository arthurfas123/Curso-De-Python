from math import hypot
print(f'Calcúlando hipótenusa!!!')
print('=-=' * 20)
cato = float(input('Cateto oposto: '))
cata = float(input('Cateto adjacente: '))
print(f'Hipotenusa: {hypot(cato, cata):.2f}')
