palavras = ('batata', 'pedro', 'laura')
cont = 0
a = ['a', 'e', 'i', 'o', 'u']

for p in palavras:
    print(f'\nNa palavra {p.upper()} remos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')