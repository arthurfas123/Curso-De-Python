print('CAÇANDO VOGAIS!!!')
print('=-=' * 15)
palavras = ('Faca', 'Dado', 'Bicicleta', 'Notebook', 'Livro', 'Porta', 'Python')
for c in palavras:
    print(f'\n{c}: ', end='')
    for u in c:
        if u.lower() in 'aeiou':
            print(u, end=' ')
