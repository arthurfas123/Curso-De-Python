print('LENDO VARIOS USUARIOS!!!')
print('=-=' * 15)
maior = homens = mulher = 0
continuar = ''
while True:
    idade = int(input('IDADE: '))
    if idade > 18:
        maior += 1
    sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
    if sexo not in 'FM':
        print('Opção \033[31minvalida!\033[m ...tente novamente.')
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulher += 1
    continuar = str(input('Deseja cadastrar outro usuario [S/N]: ')).upper().strip()[0]
    print('=-=' * 15)
    if continuar in 'N':
        break
print(f'Foram cadastrados {maior} pessoas maiores de idade.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulher} mulheres com menos de 20 anos.')
