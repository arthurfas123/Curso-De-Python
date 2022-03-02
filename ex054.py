from datetime import date
print('Maioridade!!!')
print('=-=' * 15)
maior = menor = 0
data = date.today().year
for c in range(1, 8):
    n = int(input(f'Ano de nascimento da {c} pessoa: '))
    if data - n >= 18:
        maior += 1
    else:
        menor += 1
print('=-=' * 15)
print(f'{maior} Pessoas cadastradas são maiores.')
print(f'{menor} Pessoas cadastradas são menores.')
