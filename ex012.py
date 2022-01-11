n1 = float(input('Qual o valor do produto?'))
n2 = float(input('Quantos porcentos de desconto?'))

n3 = n1 * (n2/100)

print(f'O valor do desconto é {n3} totalizando {n1-n3}')