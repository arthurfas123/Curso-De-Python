print('Extraindo dados de uma lista!!!')
n = []
while True:
    continuar = 's'
    print('=-=' * 15)
    n.append(int(input('Digite um valor: ')))
    print('=-=' * 15)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
        if continuar not in 'SN':
            print('=-=' * 15)
            print('\033[31mERRO...\033[m Valor invalido!!!')
    if continuar in 'N':
        break
n.sort(reverse=True)
print('=-=' * 15)
print(f'Foram digitados {len(n)} valores.')
print(f'Numeros em ordem decrescente {n}.')
for i, v in enumerate(n):
    if v == 5:
        print(f'o numero 5 foi encontrado na posição {i}.')
if 5 not in n:
    print('O numero 5 não foi encontrado.')
