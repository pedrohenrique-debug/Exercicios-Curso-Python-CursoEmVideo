numeros = []
while True:
    numeros.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} numeros')
print(f'Em ordem decrescente fica {numeros}')
if 5 in numeros:  # O 5 esta nos valores
    print(f'O numero 5 foi digitado na lista')
else:  # se não estiver
    print('O valor 5 não foi encontrado na lista!')