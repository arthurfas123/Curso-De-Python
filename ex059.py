print('MENU!!!')
print('=-=' * 15)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('=-=' * 15)
while True:
    menu = int(input('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR
    OPÇÃO: '''))
    print('=-=' * 15)
    if menu == 1:
        print(f'SOMA: {n1 + n2}')
        print('=-=' * 15)
    if menu == 2:
        print(f'MULTIPLICAÇÃO: {n1 * n2}')
        print('=-=' * 15)
    if menu == 3:
        if n1 > n2:
            print(f'MAIOR: {n1}')
            print('=-=' * 15)
        else:
            print(f'MAIOR: {n2}')
            print('=-=' * 15)
    if menu == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
        print('=-=' * 15)
    if menu == 5:
        break
print('OBRIGADO POR ESCOLHER NOSSO SERVIÇO.')
