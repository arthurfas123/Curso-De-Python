def ficha(goals=0, name='<Desconhecido>'):
    print(f'O jogador {name} fez {goals} gols no campeonato.')


nome = str(input('NOME: '))
gols = str(input('GOLS: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(goals=gols)
else:
    ficha(name=nome, goals=gols)

