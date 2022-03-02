print('Calculando media!!!')
print('=-=' * 20)
n1 = int(input('Primeira nota: '))
n2 = int(int(input('Segunda nota: ')))
print('=-=' * 20)
media = (n1 + n2) / 2
if media >= 70:
    print(f'Media: {media}, \033[34mAPROVADO!')
elif 50 < media < 70:
    print(f'Media: {media}, \033[33mRECUPERAÇÃO!')
elif media < 50:
    print(f'Media: {media}, \033[31mRETIDO!')
