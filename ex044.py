print(f'{" LOJAS HENRIQUE ":=^40}')
valor = float(input('Qual o valor? '))
print('1: À vista dinheiro')
print('2: À vista no cartão')
print('3: 2x no cartão')
print('4: 3x no cartão')
opcao = int(input('Digite a opção: '))





if opcao == 1:
    a = valor - (valor * 10 / 100)

elif opcao == 2:
    a = valor - (valor * 5 / 100)
elif opcao == 3:
    a = valor
elif opcao == 4:
    a = valor + (valor * 20 / 100)
    parcela = int(input('Quantas parcelas?'))
    print(f'Sua compra será parcelada em {parcela}x de R${a/parcela:.2f} com juros')

else:
    a = valor
    print('Erro! Selecione uma opção valida!')
print(f'Valor a ser pago é R${a:.2f}')



