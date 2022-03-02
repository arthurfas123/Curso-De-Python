from datetime import date


def voto(a):
    idade = data - nascimento
    if idade < 16:
        return f'Idade: {idade}, VOTO NEGADO'
    elif 18 > idade >= 16 or idade >= 65:
        return f'Idade: {idade}, VOTO OPÇIONAL'
    elif idade >= 18:
        return f'Idade: {idade}, VOTO OBRIGATORIO'


data = date.today().year
nascimento = int(input('Ano De Nascimento: '))
print(voto(nascimento))
