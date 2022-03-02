def leiaint(n):
    while True:
        msg = str(input(f'{n}'))
        if msg.isnumeric():
            msg = int(msg)
            break
        else:
            print(f'\033[31mNumero inteiro invalido!\033[m')
    return msg

numero = leiaint('Digite um valor: ')
print(f'Voce digitou o numero inteiro {numero}.')
