matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
print('-=' * 30)
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()












# linha1 = list()
# linha2 = list()
# linha3 = list()
# for c in range(0, 3):
#     linha1.append(int(input(f'Digite um avalor para [0, {c}]: ')))
# for c in range(0, 3):
#     linha2.append(int(input(f'Digite um avalor para [1, {c}]: ')))
# for c in range(0, 3):
#     linha3.append(int(input(f'Digite um avalor para [2, {c}]: ')))
# print(f"[ {linha1[0]} ][ {linha1[1]} ][ {linha1[2]} ]")
# print(f"[ {linha2[0]} ][ {linha2[1]} ][ {linha2[2]} ]")
# print(f"[ {linha3[0]} ][ {linha3[1]} ][ {linha3[2]} ]")

















# linha2 = ['4']
# linha3 = ['7', '8', '9']
#
# print(f"[ {', '.join(linha2)} ]")
# print(linha2)
# print(linha3)