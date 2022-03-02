print('CALCULANDO UMA PA!!!')
print('=-=' * 15)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('=-=' * 15)
print('PA:')
for c in range(p, p + (r * 10), r):
    print(c, end='-->')
print('ACABOU!!!')