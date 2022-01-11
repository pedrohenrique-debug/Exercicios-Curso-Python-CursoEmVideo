from datetime import date
a = date.today().year

n = 0
n1 = 0
for c in range(0, 7):
    data = int(input('Data nascimento: '))
    if a - data >= 21:
        n = n + 1
    else:
        n1 = n1 + 1
print(f'{n} são de maiores e {n1} são de menores')
