from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha com sabedoria
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*11)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador VENCEU')
    elif jogador == 2:
        print('Jogador PERDEU')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPÇÂO INVALIDA')






'''import random
from time import sleep

print('Escolha com sabedoria')

print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
opcao = int(input('Opção desejada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

pc = random.randint(1,3)
if opcao == 1 and pc == 1 or opcao == 2 and pc == 2 or opcao == 3 and pc == 3:
    print('Empate')

elif opcao == 1 and pc == 2 or opcao == 2 and pc == 3 or opcao == 3 and pc == 1:
    print('Você perdeu')
elif opcao == 1 and pc == 3 or opcao == 2 and pc == 1 or opcao == 3 and pc == 1:
    print('Você ganhou')
print('-=' * 20)'''
