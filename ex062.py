print('Progressão Aritimetica V3.0!!!')
print('=-=' * 15)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
pa = pt
nt = 10
total = 0
print('=-=' * 15)
while nt != 0:
    total += nt
    while cont < total:
        cont += 1
        if cont == 1:
            print(f'{pt}', end=' = ')
        else:
            pa += razao
            if cont == 10:
                print(f'{pa}', end=' = ')
            else:
                print(f'{pa}', end=' = ')
    print('PAUSA')
    print('=-=' * 15)
    nt = int(input('Quantos termos novos deseja ver: '))
