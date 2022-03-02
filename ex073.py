print('TABELA DO BRASILEIRÃO!!!')
print('=-=' * 15)
times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Bragantino', 'Ceará',
         'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional',
         'Juventude', 'Palmeiras', 'Santos', 'São Paulo')
print(f'5 Primeiros colocados: {times[0:6]}')
print(f'4 Ultimos colocados: {times[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O time do fluminense esta na {times.index("Fluminense") + 1} Colocação.')
