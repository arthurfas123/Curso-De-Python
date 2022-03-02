print('Introdução a dicionario!!!')
print('=-=' * 15)
dados = dict()
dados['nome'] = str(input('NOME: '))
dados['media'] = float(input('MEDIA: '))
if dados['media'] < 60:
    dados['situacao'] = 'REPROVADO'
elif dados['media'] >= 60:
    dados['situacao'] = 'APROVADO'
print('=-=' * 15)
print(dados)
