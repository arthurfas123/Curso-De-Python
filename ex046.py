from time import sleep
print('ANO NOVO!!!')
print('=-=' * 15)
print('Atenção para a contagem regressiva.')
print('=-=' * 15)
for c in range(10, -1, -1):
    print(f'\033[31m{c}')
    sleep(1)
print('\033[m=-=' * 15)
print('\033[34mFeliz Ano Novo!!!')
