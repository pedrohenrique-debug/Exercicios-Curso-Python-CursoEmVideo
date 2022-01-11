frase = str(input('Digite uma frase: ')).strip().replace(' ', '')
a = frase[::-1]
print(f'O inverso de {frase} é {a} ')
if a == frase:

    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
