import moedas
valor = int(input('Valor: '))
taxa = int(input('Taxa % : '))
moedas.linha()
print(f'Aumento de {taxa}%: {moedas.aumentar(valor, taxa)}')
print(f'Menos {taxa}%: {moedas.diminuir(valor, taxa)}')
print(f'Dobro: {moedas.dobro(valor)}')
print(f'Metade: {moedas.metade(valor)}')
