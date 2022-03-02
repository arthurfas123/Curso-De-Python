# Formatando moedas em python
from ex108 import moedas
valor = int(input('Valor: '))
taxa = int(input('Taxa % : '))
moedas.linha()
print(f'Aumento de {taxa}%: {moedas.formatando(moedas.aumentar(valor, taxa))}')
print(f'Menos {taxa}%: {moedas.formatando(moedas.diminuir(valor, taxa))}')
print(f'Dobro: {moedas.formatando(moedas.dobro(valor))}')
print(f'Metade: {moedas.formatando(moedas.metade(valor))}')
