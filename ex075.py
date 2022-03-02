print('GUARDANDO VALORES EM TUPLAS!!!')
print('=-=' * 15)
n = (int(input('1 numero: ')), int(input('2 numero: ')), int(input('3 numero: ')), int(input('4 numero: ')))
print('=-=' * 15)
print(f'O numero 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O numero 3 aparece pela primeira vez na posição {n.index(3) + 1}')
else:
    print('O numero 3 não foi adicionado.')
print('Os numeros pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
print()
