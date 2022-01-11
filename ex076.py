listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.22, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
        print('-' * 40)















# print('--' * 20)
# print('          LISTAGEM DE PREÇOS')
# print('--' * 20)
# a = cont = 0
# b = 1
# while True:
#     print(f'{lista[a]}..........R$ {lista[b]:.2f}')
#     a += 2
#     b += 2
#     cont += 1
#     if cont == 9:
#         break
