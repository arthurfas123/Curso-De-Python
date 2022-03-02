print('Classificando triangulos!!!')
print('=-=' * 20)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
print('=-=' * 20)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('È possivel formar um triangulo!')
    print('=-=' * 20)
    print('Classificação: ', end='')
    if l1 == l2 == l3:
        print('equilatero.')
    elif l1 != l2 != l3:
        print('ESCALENO!')
    else:
        print('ISOSCELES.')
else:
    print('NÂO é possivel formar triangulo!')
