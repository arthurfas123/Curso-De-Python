print('Analisando emprestimos!!!')
print('=-=' * 20)
valor = float(input('Valor do imovel: R$'))
salario = float(input('Salario do cliente: R$'))
tempo = int(input('Tempo do emprestimo [anos]: '))
print('=-=' * 20)
if valor / (12 * tempo) >= salario * 30/100:
    print(f'Seu emprestimo foi \033[31mNEGADO!')
else:
    print('Seu emprestimo foi \033[34mAPROVADO!')
