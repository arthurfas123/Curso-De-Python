print('LENDO PRODUTOS!!!')
print('=-=' * 15)
continuar = nbarato = ''
total = pmil = cont = pbarato = 0
while True:
    cont += 1
    nome = str(input('NOME: '))
    preco = float(input('PREÇO: '))
    continuar = str(input('CADASTRAR OUTRO PRODUTO [S/N]: ')).upper().strip()[0]
    total += preco
    if preco > 1000:
        pmil += 1
    if cont == 1:
        nbarato = nome
        pbarato = preco
    elif cont != 1 and preco < pbarato:
        nbarato = nome
        pbarato = preco
    print('=-=' * 15)
    if continuar in 'N':
        break
print(f'VALOR: {total}')
print(f'Foram cadastrados {pmil} produtos acima de R$1000.')
print(f'O produto mais barato foi {nbarato} e custa R${pbarato}')
