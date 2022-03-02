# 1 METODO
from random import choice
#print('Sorteando alunos!!!')
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Segundo aluno: '))
#n3 = str(input('Terceiro aluno: '))
#n4 = str(input('Quarto aluno: '))
#lista = [n1, n2, n3, n4,]
#print(f'O aluno escolhido foi: {choice(lista)}')

# 2 METODO
nomes = list()
for c in range(1, 5):
     nomes.append(str(input(f'{c} Aluno: ')))
print(f'O aluno escolhido foi: {choice(nomes)}')
