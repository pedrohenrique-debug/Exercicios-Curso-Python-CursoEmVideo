num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mNumero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por iss ele é primo')
else:
    print('E por isso ele não é primo')