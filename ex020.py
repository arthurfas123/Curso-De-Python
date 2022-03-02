from random import shuffle
print('Ordem de apresentação!!!')
nomes = list()
for c in range(1, 5):
    nomes.append(str(input(f'{c} Nome: ')))
shuffle(nomes)
print(f'A Ordem de apresentação sera: {nomes})')
