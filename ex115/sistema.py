from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        # Opção de listar o conteudo de um arquivo.
        lerArquivo(arq)
    elif resp == 2:
        # Opção para cadastrar novo usuario.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        # Opção para sair do menu.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mErro: Digite uma opção valida!\033[m')
    sleep(2)
