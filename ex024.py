cidade = str(input('Qual o nome da cidade?')).strip()
a = cidade.upper().split()
b = 'SANTO' in a[0]
print(f'Essa cidade começa com santo? {b}')