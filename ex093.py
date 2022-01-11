jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')






# jogador = {'nome': '', 'gols': [], 'total': ''}
#
# jogador['nome'] = str(input('Nome do jogador: '))
# part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#
# for c in range(0, part):
#     jogador['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
# jogador['total'] = sum(jogador['gols'])
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# print(f'O campo nome tem o valor {jogador["nome"]}.')
# print(f'O camo gols tem o valor {jogador["gols"]}.')
# print(f'O campo total tem valor {jogador["total"]}')
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
#
# cont = 0
# for c in jogador['gols']:
#     print(f'=> Na partida {cont}, fez {c} gols.')
#     cont += 1
# print(f'Foi um total de {sum(jogador["gols"])} gols.')
#
#
#
