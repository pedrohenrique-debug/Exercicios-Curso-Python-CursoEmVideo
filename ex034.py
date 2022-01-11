sal = float(input('Qual o seu salário? '))

if sal >= 1250:
    p = (sal*10)/100
    print(f'Seu aumento foi de R${p:.2f}, totalizando R${sal+p:.2f} reais')
else:
    m = (sal*15)/100
    print(f'Seu aumento foi de R${m:.2f}, totalizando R${sal+m:.2f} reais')