print('NUMEROS POR EXTENSO!!!')
print('=-=' * 15)
numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Escolha um numero entre 0 e 20: '))
    print('=-=' * 15)
    if -1 < n < 21:
        print(f'Numero {n}: {numeros[n]}')
        break
    print('Opção invalida!')
    print('=-=' * 15)
