# Formatando moeds em python
from ex109 import moedas
valor = int(input('Valor: '))
taxa = int(input('Taxa % : '))
moedas.linha()
print(f'Aumento de {taxa}%: {moedas.aumentar(valor, taxa, True)}')
print(f'Menos {taxa}%: {moedas.diminuir(valor,taxa, True)}')
print(f'Dobro: {moedas.dobro(valor, True)}')
print(f'Metade: {moedas.metade(valor, True)}')
