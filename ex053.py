print('Detectando palindromos!!!')
print('=-=' * 15)
frase = str(input('Diga uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('=-=' * 15)
for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('A frase É PALINDROMO.')
else:
    print('A frase NÃO É PALINDROMO.')
