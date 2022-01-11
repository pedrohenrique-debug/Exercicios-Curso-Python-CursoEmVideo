cores = {'limpar':'\033[m',
         'azul':'033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m'}
nome = str(input('Qual é o seu nome? '))
print('-='*20)
print(f'Olá {nome}! Escolha uma cor!')
print('-='*20)
print(f'1:{cores['azul']} 'Azul' {cores['limpar']}')
print('2:\033[33mAmarelo\033[m')
print(f'3:\033[31mVermelho\033[m')
print('-='*20)
cor = int(input('Digite o numero aqui: '))
print('-='*20)
if cor == 1:
    print('Você escolheu a cor azul. Uma bela cor :)')
print('-=' * 20)
cor1 = str(input('Você sabe o que ela significa?')).upper().strip()
print('-='*20)
if cor1 == 'SIM':
    print(f'Muito bom você saber. {nome} cor Azul simboliza lealdade, confiança e tranquilidade.  ')

