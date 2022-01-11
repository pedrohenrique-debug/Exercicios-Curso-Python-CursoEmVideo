from time import sleep
opcao = 0
cont = 0
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

while opcao != 5:
    print('=-='*15)
    print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos numeros
        [5] Sair do programa
    ''')

    opcao = int(input('>>>>>Digite a opção: '))
    if opcao == 1:
        r = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {r}')
    elif opcao == 2:
        r = n1 * n2
        print(f'A multiplicação de {n1} por {n2} é igual a {r}')
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        print('Informe novos números')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
        print('=-='*15)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção inválida. Tente novamente.')








