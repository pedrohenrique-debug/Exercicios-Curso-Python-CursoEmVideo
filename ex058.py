from random import randint
computador = randint(0, 10)
usuario = 0
cont = 0

print('-=' * 20)
print('Pense em um número de 0 a 10')
print('-=' * 20)
while usuario != computador:
    usuario = int(input('Digite um numero: '))
    if usuario < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    cont += 1

if cont == 1:
    print('Parabéns você acertou de primeira')

else:
     print(f'Você acertou em {cont} tentativas, parabéns')

