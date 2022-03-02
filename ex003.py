print('SOMANDO DOIS NUMEROS!!!')
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo nunmero: '))
soma = n1 + n2
print(f'O RESULTADO DA SOMA È {soma}')
print('')

# PROCESSO 2

print('=-=' * 25)
soma2 = 0
r = 0
while True:
    n = int(input('DIgite um numero: '))
    soma2 += n
    r += 1
    if r >= 2:
        break
print(f'O RESULTADO DA SOMA È {soma2}')

# PROCESSO 3

print('=-=' * 25)
t = 0
for c in range(0, 2):
    t += int(input('Digite um numero: '))
print(t)
