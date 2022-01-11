n =int(input(('Digite um número para calcular o seu Fatorial: ')))
c = n
f = 1
print(f'Calculando {n}!= ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')





'''n1 = int(input('Digite um numero: '))
n2 = n1
n3 = n1
for c in range(n-1, 1, -1):
    r = n * c
    n = r
print(f'O fatorial de {n1} é {n}')
while n1 > 1:
    r = n1 - 1
    n1 = r
    s = n2 * n1
    n2 = s


print(f'O fatorial de {n3} é {n2}')'''


