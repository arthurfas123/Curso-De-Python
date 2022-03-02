def notas(*notas, sit=False):
    """
    => Função que lê uma quantidade indefinida de notas e retorna um dicionario
     com quantidade de notas, notas, maior nota, menor nota, media e situação
     como um parametro opçional.
    :param notas: quantidade indefinida de notas de um determinado aluno.
    :param sit: (Opçional) parametro de valor real que define se ira ou nao retornar a situaçao do aluno
    (Ruim, Razoavel, bom).
    :return: retorna um dicionario com todas as informações.
    """
    dados = dict()
    dados['quantidade de notas'] = len(notas)
    dados['notas'] = notas
    dados['maior notas'] = max(notas)
    dados['menor nota'] = min(notas)
    dados['media'] = sum(notas) / len(notas)
    if sit:
        if dados['media'] < 6:
            dados['situação'] = 'Ruim!'
        elif dados['media'] >= 8:
            dados['situação'] = 'Boa!'
        else:
            dados['situação'] = 'Razoavel'
    return dados


dicionario = notas(3, 8, 9, sit=True)
print(dicionario)
