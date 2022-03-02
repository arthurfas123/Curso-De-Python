print('Media em lista composta!!!')
print('=-=' * 15)
alunos = []
while True:
    continuar = 's'
    alunos.append([])
    alunos[len(alunos) - 1].append(str(input('NOME: ')))
    alunos[len(alunos) - 1].append(int(input('1 NOTA: ')))
    alunos[len(alunos) - 1].append(int(input('2 NOTA: ')))
    while continuar not in 'SN':
        continuar = str(input('Cadastrar novo aluno [S/N]: ')).upper().strip()[0]
        print('=-=' * 15)
        if continuar not in 'SN':
            print('OPÇÂO INVALIDA... Tente Novamente!')
    if continuar in 'N':
        break
print(f'{"No.":<4}{"NOME":<15}{"MEDIA":>8}')
print('=-=' * 15)
for c in range(0, len(alunos)):
    print(f'{c} {alunos[c][0]:<10}: {(alunos[c][1] + alunos[c][2]) / 2:>8.1f}')
while True:
    continuar = 's'
    while continuar not in 'SN':
        print('=-=' * 15)
        continuar = str(input('Deseja ver alguma nota [S/N]: ')).upper().strip()[0]
        if continuar not in 'SN':
            print('OPCÂO INVALIDA... Tente Novamente!')
    if continuar in 'N':
        break
    n = int(input('Qual aluno deseja ver: '))
    print('=-=' * 15)
    print(f'As notas do(a) {alunos[n][0]} foram: {alunos[n][1]}, {alunos[n][2]}')
