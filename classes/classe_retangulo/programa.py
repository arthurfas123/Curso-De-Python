import classe_retangulo
ladoA = float(input('LadoA [M]: '))
ladoB = float(input('ladoB [M]: '))
piso = 0.3
retangulo = classe_retangulo.Retangulo(ladoA, ladoB)
area = retangulo.calcularArea()
cont = npiso = 0
while cont < area:
    npiso += 1
    cont += piso
print(f'Será utilisado no minimo {npiso} pisos')
