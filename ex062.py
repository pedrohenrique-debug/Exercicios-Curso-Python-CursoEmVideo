primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:

        print(f'{termo}-', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
