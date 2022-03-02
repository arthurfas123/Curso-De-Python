print('Radar eletronico!!!')
print('=-=' * 20)
velocidade = float(input('Qual a velocidade do carro: KM'))
print('=-=' * 20)
if velocidade > 80:
    print('Você foi \033[31mMULTADO!\033[m')
    print(f'A multa será R${7 * (velocidade - 80):.2f}')
else:
    print('\033[34mVocê passou dentro do limite de velocidade!\033[m')
