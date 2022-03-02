print('Par ou Impar!!!')
print('=-=' * 20)
n = int(input('Digite um numero: '))
print('=-=' * 20)
if n % 2 == 0:
    print('\033[34mPAR.\033[m')
else:
    print('\033[31mIMPAR.\033[m')
