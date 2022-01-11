homem = mulher = mais = menos = conti = contm = contf = 0
while True:
    print('--' * 15)
    print('     CADASTRE UMA PESSOA')
    print('--' * 15)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    print('--' * 15)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer contnuar? [S/N] ')).upper().strip()[0]
    if sexo in 'M':
        contm += 1
    if idade > 18:
        conti += 1
    elif sexo in 'F' and idade < 20:
        contf += 1

    if continuar in 'N':
        break

print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {conti}')
print(f'Ao todo temos {contm} homens cadastrados')
print(f'E temos {contf} mulheres com menos de 20 anos')
