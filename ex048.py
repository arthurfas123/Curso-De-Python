print('SOMA DE NUMEROS IMPARES!!!')
print('=-=' * 15)
cont = soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'O resultado da soma de todos os \033[31m{cont}\033[m numeros impares entre 1 e 500 é \033[31m{soma}.')
