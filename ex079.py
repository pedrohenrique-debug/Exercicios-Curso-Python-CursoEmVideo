numeros = []
while True:
    num = int(input('Digite um valor'))


    if num not in numeros:
        numeros.append(num)
        print('Valores adcionados com sucesso')
    else:
        print('Erro, esse valor já existe')

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')
print('FIM')