from ex113 import leiaInt
c = ('\033[m',         # 0 sem cor
     '\033[0;31m',  # 1 vermelho
     '\033[0;32m',  # 2 verde
     '\033[7;40m',  # 3 branco
     '\033[0;34m',  # 4 azul
     '\033[0;33m',  # 5 amarelo
     )
dados = []
while True:
    while True:
        print('=-=' * 15)
        print('\t\t\tMENU PRINCIPÁL')
        print('=-=' * 15)
        print(f'''{c[5]}\t\t1- {c[4]}Ver usuarios cadastrados.
        {c[5]}2- {c[4]}Cadastrar novo usuario.
        {c[5]}3- {c[4]}SAIR.''')
        opção = leiaInt(f'{c[2]}\t\tOPÇÂO: {c[0]}')
        print('=-=' * 15)
        break
    if opção == 1:
        print(f'{"   NOME"}{"idade":>22}')
        print('=-=' * 15)
        for usuario in dados:
                print(f'\t{usuario["nome"]}\t\t\t\t{usuario["idade"]}')
    if opção == 2:
        novo_usuario = {}
        novo_usuario['nome'] = (str(input('Nome: ')))
        novo_usuario['idade'] = leiaInt('Idade: ')
        dados.append(novo_usuario)
    if opção == 3:
        break
print(f'{c[1]}Encerrando Programa... Volte sempre!{c[0]}')
print('=-=' * 15)
