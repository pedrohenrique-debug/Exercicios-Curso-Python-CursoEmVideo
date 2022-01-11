from datetime import date
data = int(input('Qual o ano de nascimento? '))

ano = date.today().year

idade = ano - data
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria mirim')
elif idade <= 14:
    print('Categoria infantil')
elif idade <= 19:
    print('Categoria junior')
elif idade <= 25:
    print('Categoria sênior')
else:
    print('Categoria master')