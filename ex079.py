print('VaLores unicos em uma lista')
print('=-=' * 15)
n1 = []
continuar = 's'
while True:
    continuar = 's'
    while continuar not in 'SN':
        continuar = str(input('Cadastrar novo valor [S/N]: ')).upper().strip()
        if continuar not in 'SN':
            print('Valor invalido! Tente novamente...')
    if continuar in 'N':
        break
    n2 = int(input('Digite um valor: '))
    print('=-=' * 15)
    if n2 not in n1:
        n1.append(n2)
    else:
        print('ERRO... Valor duplicado!')
print('=-=' * 15)
n1.sort()
print(f'Os valores unicos digitados foram: {n1}')
