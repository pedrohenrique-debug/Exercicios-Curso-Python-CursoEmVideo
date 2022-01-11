numeros = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)

    if 'N' in opcao:
        break

print(numeros)
print(par)
print(impar)