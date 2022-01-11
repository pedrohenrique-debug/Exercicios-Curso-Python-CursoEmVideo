expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressão esta errada!')

# a = ['(']
# print(a[0].count('('))
# if 'a' in a[0]:
#     print('Sim')

#
# p.append(str(input('Digite a expressão: ')))
#
# a = p[0].count('(')
# b = p[0].count(')')
# c = a + b
# if c % 2 == 0:
#     print('Essa expressão é valida')
# else:
#     print('Essa expressão é invalida!')

# print(a)
# print(b)
# print(a + b)
