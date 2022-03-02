print('Conversão de bases numericas!!!')
print('=-=' * 20)
n = int(input('Digite um numero qualquer: '))
print('=-=' * 20)
print('''Escolha qual a base de conversão:
[1] Binario
[2] Octal
[3] Hexadecimal''')
b = int(input('Base numerica: '))
print('=-=' * 20)
if b == 1:
    c = bin(n)
    print(f'O numero {n} em base Binaria é \033[34m{c[2:]}.')
elif b == 2:
    c = oct(n)
    print(f'O numero {n} em base Octal é \033[34m{c[2:]}.')
elif b == 3:
    c = hex(n)
    print(f'O numero {n} em base Hexagonal é \033[34m{c[2:]}')
else:
    print('Opção invalida. Tente novamente!')
