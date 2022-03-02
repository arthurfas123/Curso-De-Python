print('validando expressões matematicas!!!')
print('=-=' * 15)
n = str(input('Digite uma expressão: '))
n2 = []
for c in n:
    if c == '(':
        n2.append('(')
    elif c == ')':
        if len(n2) > 0:
            n2.pop()
        else:
            n2.append(')')
            break
print('=-=' * 15)
if len(n2) == 0:
    print('A expressão anterior esta correta.')
else:
    print('A expressão anterior não esta correta.')
