from math import radians, sin, cos, tan
print('Calculando SEN, COS, TAN!!!')
print('=-=' * 20)
ângulo = float(input('Digite o ângulo: '))
print(f'SEN: {sin(radians(ângulo)):.2f}')
print(f'COS: {cos(radians(ângulo)):.2f}')
print(f'TAN: {tan(radians(ângulo)):.2f}')
