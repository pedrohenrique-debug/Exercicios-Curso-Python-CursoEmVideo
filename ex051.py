n = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
d =  n + (10 - 1) * r
for c in range(n, d + r, r):
    print(c, end='→')
print('ACABOU')
