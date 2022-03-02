# Formatando moedas em python
from ex112.utilidadescev import moedas
from ex112.utilidadescev import dados
valor = dados.leiaDinheiro('Valor: ')
moedas.resumo(valor, 10, 20)
