print('='*30)
print(' Banco Rique')
print('='*30)
valor = int(input('Quanto você quer sacar? R$'))
total = valor
c = 50
cont = 0
while True:
    if  total >= c:
        total -= c
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        cont = 0
        if total == 0:
            break
