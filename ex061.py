primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}-', end='')
    termo += razao
    cont += 1
print('Acabou')