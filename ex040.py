nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota?'))

media = (nota1 + nota2)/2

if media < 5:
    print('Reprovado')
elif media >=5 and media <= 6.9:
    print('Recuperação')

else:
    print('Aprovado')
