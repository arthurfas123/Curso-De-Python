print('Calculando IMC!!!')
print('=-=' * 20)
altura = float(input('Altura [m]: '))
peso = float(input('Peso [Kg]: '))
imc = peso / (altura ** 2)
print('=-=' * 20)
print('Classificação: ', end='')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
elif 40 <= imc:
    print('Obesidade morbida.')
