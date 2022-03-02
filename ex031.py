print('Calculando viagen!!!')
print('=-=' * 20)
km = float(input('Qual a distancia da viagen: Km'))
print('=-=' * 20)
if km <= 200:
    print(f'A viagen irá custar R${0.50 * km:.2f}')
else:
    print(f'A viagen irá custar R${0.45 * km:.2f}')
