print('SUPERMERCADO ARAGUAIA!!!')
print('=-=' * 20)
preco = float(input('Preço: R$'))
print('=-=' * 20)
print('''Pagamento:
[1] Avista Dinheiro/cheque
[2] Avista No Cartão
[3] Em Ate Duas Vezes No Cartão
[4] 3x Ou mais No Cartão''')
alternativa = int(input('Forma De Pagamento: '))
print('=-=' * 20)
if alternativa == 1:
    preco = preco - (preco * 10/100)
    print('DESCONTO: 10%')
    print(f'PREÇO: {preco}')
elif alternativa == 2:
    preco = preco - (preco * 5/100)
    print('DESCONTO: 5%')
    print(f'PREÇO: {preco}')
elif alternativa == 3:
    print('SEM DESCONTO.')
    parcelas = int(input('PARCELAS: '))
    print(f'PREÇO: {parcelas} parcela De R${preco / parcelas:.2f}')
elif alternativa == 4:
    preco = preco + (preco * 20/100)
    print('JUROS: 20%')
    parcelas = int(input('PARCELAS: '))
    print(f'PREÇO: {parcelas} Parcelas De R${preco / parcelas:.2f}')
print('OBRIGADO PELA PREFERENCIA!')
