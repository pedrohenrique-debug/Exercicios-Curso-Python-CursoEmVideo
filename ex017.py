'''catetoop = float(input('Qual o cateto oposto? '))
catetoad = float(input('Qual o cateto adjacente? '))

hipotenusa = (catetoad **2 + catetoop **2) ** (1/2)
print(f'O valor da hipotenusa é {hipotenusa:.2f}')'''
from math import hypot
co = float(input('Qual cateto oposto?'))
ca = float(input('Qual cateto adjacente?'))

res = hypot(co, ca)

print(f'A hipotenusa é {res:.2f}')