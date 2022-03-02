print('Separando numeros!!!')
print('=-=' * 20)
while True:
    num = int(input('Digite um numero: '))
    print('=-=' * 20)
    if 0 < num < 9999:
        milhar = num // 1000 % 10
        centena = num // 100 % 10
        dezena = num // 10 % 10
        unidade = num // 1 % 10
        print(f'Milhar: {milhar}')
        print(f'Centena: {centena}')
        print(f'Dezena: {dezena}')
        print(f'Unidade: {unidade}')
        break
    print('NUMERO INVALIDO!!! TENTE NOVAMENTE.')
