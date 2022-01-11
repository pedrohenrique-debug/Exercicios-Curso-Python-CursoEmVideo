totcont = maisdemil = barato = caro = cont = 0
nomebarato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))

    totcont += preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    cont += 1
    if cont == 1 or preço < barato:
        barato = preço
        nomebarato = nome



    if preço > 1000:
        maisdemil += 1
    if continuar in 'N':
        break
print(f'O total da compra foi R${totcont:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}')
