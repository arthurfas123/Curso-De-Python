print('TABUADA V3.0!!!')
cont = 0
while True:
    print('=-=' * 15)
    n1 = int(input('Digite um numero (negativo para finalizar): '))
    print('=-=' * 15)
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{n1} X {c:2} = {n1 * c}')
print('Obrigado por usar nosso sistema!')
