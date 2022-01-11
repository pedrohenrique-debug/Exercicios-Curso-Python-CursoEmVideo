from datetime import date

n = int(input('Quando você nasceu? '))
ano = date.today().year

print(f'Quem nasceu em {n} tem {ano-n} em {ano}')
if ano - n < 18:
    a = 18 - (ano - n)
    print('Você ainda vai se alistar pro exercito')
    print(f'Faltam {a} anos para isso acontecer.')
    print(f'Seu alistamento deverá ser feito em {ano + a}.')
elif ano - n == 18:
    print('Esta na hora de se alistar')

elif ano - n > 18:
    b = (ano - n) - 18
    print('Passou da hora de se alistar')
    print(f'Passou {b} anos da data de alistamento.')
    print(f'Seu alistamento deveria ter sido em {ano - b}.')

