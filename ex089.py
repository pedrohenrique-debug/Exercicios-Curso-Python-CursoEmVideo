ficha = list()
while True:
    nome = str(input('Nome '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe: )'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')











# alunos = list()
# nomes = list()
# nota1 = list()
# nota2 = list()
# media = list()
# while True:
#     nomes.append(str(input('Nome: ')))
#     nota1.append(str(input('Nota 1: ')))
#     nota2.append(str(input('Nota 2: ')))
#
#     continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if continuar in 'N':
#         break
# alunos.append(nomes)
# alunos.append(nota1)
# alunos.append(nota2)
# nota = [int(item) for item in nota1 if item.isdigit()]
# notal = [int(item) for item in nota2 if item.isdigit()]
# print('-=' * 30)
# print('No. NOME    MÉDIA')
# print('-' * 20)
#
# for c in range(len(alunos[0])):
#     media = (nota[c]+notal[c])
#     print(f'{c:<3} {alunos[0][c]:<9} {media*0.5} ')
# while True:
#     for c in range(len(alunos[0])):
#
#         mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#         if mostrar in c:
#             print(f'As notas de {alunos[0][c]} são {nota1[c]}, {nota2[c]}')
#             c += 1
#     if mostrar == 999:
#         break
# # nomes[0] nota1[0] + nota2[0]/2