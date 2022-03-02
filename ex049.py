print('TABUADA V2.0')
print('=-=' * 15)
n = int(input('Digite um numero para ver sua tabuada: '))
print('=-=' * 15)
for c in range(1, 11):
    print(f'{c:2} X {n} = {c * n}')
