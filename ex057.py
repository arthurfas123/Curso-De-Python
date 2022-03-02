print('LENDO UM VALOR ESPECIFICO!!!')
print('=-=' * 15)
while True:
    sexo = str(input('SEXO [M/F]: ')).upper()
    if sexo not in 'MF':
        print('Dado inserido invalido... Tente novamente!')
        print('=-=' * 15)
    if sexo in 'MF':
        break
print('=-=' * 15)
print('Dados validos... Cadastro completo.')
