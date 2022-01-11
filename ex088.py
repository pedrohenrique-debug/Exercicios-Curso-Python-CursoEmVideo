from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)














# from random import randint
# from time import sleep
# numeros = list()
# jogadas = list()
#
# print('-' * 30)
# print(f'{"JOGA NA MEGA SENA":^30}')
# print('-' * 30)
#
# num = int(input('Quantos jogos você quer que eu sorteie? '))
# for c in range(0, num):
#     for c in range(0, 6):
#         jogadas.append(randint(1, 60))
#     numeros.append(jogadas[:])
#     jogadas.clear()
# for c in range(0, num):
#     print(f'Jogo {c+1}: {sorted(numeros[c])}')
#     sleep(0.5)
