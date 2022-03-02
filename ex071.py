print('SIMULANDO CAIXA!!!')
print('=-=' * 15)
n = int(input('VALOR A SACAR: R$'))
cinquenta = vinte = dez = um = 0
print('=-=' * 15)
while True:
    if n % 50 == 0:
        cinquenta += 1
        n -= 50
    elif n % 20 == 0:
        vinte += 1
        n -= 20
    elif n % 10 == 0:
        dez += 1
        n -= 10
    elif n % 1 == 0:
        um += 1
        n -= 1
    if n == 0:
        break
print(f'''SERÁ SACADO:
{cinquenta} NOTAS de R$50
{vinte} NOTAS DE R$20
{dez} NOTAS DE R$10
{um} NOTAS DE R$1''')
