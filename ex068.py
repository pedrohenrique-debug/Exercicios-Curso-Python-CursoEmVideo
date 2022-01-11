from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
computador = randint(1, 10)
cont = 0
v = 0
while True:

    jogador = int(input('Digite um valor: '))
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('par ou Ímpar? [P/I]')).upper().strip()[0]
    s = jogador + computador
    print('--' * 15)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {s}. ', end='')
    print('DEU PAR' if s % 2 == 0 else 'DEU ÍMPAR')
    print('--' * 15)
    if s % 2 == 0 and opcao in 'P' or s % 2 != 0 and opcao in 'I':
        v = 1
        cont += 1
        if s % 2 == 0:
            op = 'DEU PAR'
        else:
            op = 'DEU ÍMPAR'
        print('Você venceu')
        print('Vamos jogar novamente...')
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        print('=-'*15)
        print('GAMER OVER!', end='')
        print(f'Você venceu {cont} vez.')


    if v != 1:
        break



