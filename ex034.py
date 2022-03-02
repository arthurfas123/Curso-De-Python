print('Calculando aumento!!!')
print('=-=' * 20)
salario = float(input('Qual seu salario: R$'))
print('=-=' * 20)
if salario > 1250:
    salario = salario + (salario * 10/100)
    aumento = 10
else:
    salario = salario + (salario * 15/100)
    aumento = 15
print(f'O novo salario com {aumento}% de aumento será R${salario:.2f}')
