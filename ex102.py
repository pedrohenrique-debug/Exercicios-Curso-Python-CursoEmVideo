
def fatorial(num, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num
    '''
    print('-' * 20)
    if show == False:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        print(f)
    if show == True:
        a = 1
        for c in range(num, 0, -1):
            a *= c
            print(f'{a}', end=' ')


#Programa principal
fatorial(5, show=True)

