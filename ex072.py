numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze' , 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opcao = 0
while True:
    opcao = int(input('Digite um numero entre 0 e 20: '))
    print(f'Voce digitou o número {numero[opcao]}')
    a = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if opcao not in range(0, 21):
        print('Tente novamente. ', end='')

    if 20 >= opcao >= 0 and a == 'N':
        break
print('Fim')


