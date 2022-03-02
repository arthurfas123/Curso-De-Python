print('Analizando triangulos!!!')
print('=-=' * 20)
lista = []
for c in range(0, 3):
    lista.append(float(input(f'{c} reta: ')))
if lista[0] < lista[1] + lista[2] and lista[1] < lista[0] + lista[2] and lista[2] < lista[0] + lista[1]:
    print('As retas PODEM formar um triangulo.')
else:
    print('As retas não podem formar um triangulo.')
