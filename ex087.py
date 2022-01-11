matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
print('-=' * 30)
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')

















# linha1 = list()
# linha2 = list()
# linha3 = list()
#
# pares = list()
# matriz = list()
# for c in range(0, 3):
#     linha1.append(int(input(f'Digite um avalor para [0, {c}]: ')))
# for c in range(0, 3):
#     linha2.append(int(input(f'Digite um avalor para [1, {c}]: ')))
# for c in range(0, 3):
#     linha3.append(int(input(f'Digite um avalor para [2, {c}]: ')))
# matriz.append(linha1[:])
# matriz.append(linha2[:])
# matriz.append(linha3[:])
# for v in linha1:
#     if v % 2 == 0:
#         pares.append(v)
# for v in linha2:
#     if v % 2 == 0:
#         pares.append(v)
# for v in linha3:
#     if v % 2 == 0:
#         pares.append(v)
# coluna = linha1[2] + linha2[2]+linha3[2]
# for v in linha2:
#     maior = v
#     if v > maior:
#         maior = v
#
# print('-=' * 30)
# print(f"[ {linha1[0]} ][ {linha1[1]} ][ {linha1[2]} ]")
# print(f"[ {linha2[0]} ][ {linha2[1]} ][ {linha2[2]} ]")
# print(f"[ {linha3[0]} ][ {linha3[1]} ][ {linha3[2]} ]")
# print('-=' * 30)
# print(f'A soma dos valores pares é {sum(pares)}')
# print(f'A soma dos valores da terceira coluna é {coluna}.')
# print(f'O maior valor da segunda linha é {maior}.')




