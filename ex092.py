from datetime import datetime
print('Cadastro de trabalhador!!!')
print('=-=' * 15)
dados = dict()
ano = datetime.today().year
dados['nome'] = str(input('NOME: '))
dados['ano de nascimento'] = int(input('ANO DE NASCIMENTO: '))
dados['idade'] = ano - dados['ano de nascimento']
dados['ctps'] = int(input('CARTEIRA DE TRABALHO: '))
if dados['ctps'] != 0:
    dados['ano de contratacao'] = int(input('ANO DE CONTRTATAÇÂO: '))
    dados['salario'] = int(input('SALARIO: R$'))
    dados['idade de aposentadoria'] = dados['idade'] + (dados['ano de contratacao'] + 35 - ano)
print('=-=' * 15)
for k, v in dados.items():
    print(f'  =>{k}: {v}'.upper())
