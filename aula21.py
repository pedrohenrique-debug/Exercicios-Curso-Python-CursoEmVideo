def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')
#



# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(1, 7)
# r3 = somar(4)
# print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
#
#


# Escopo variavel
# def teste():
#     global n
#     n = 5
#     print(f'Dentro n vale {n}')
#
#
# teste()
# n = 2
# print(f'Fora n vale {n}')

# parametros opcionais
# def somar(a=0, b=0, c=0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     Função criada por Pedro Henrique
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
#
# somar(3, 3, 5)




#Docstring
# def contador (i, f, p):
#     '''
#     Faz uma contagem e mostra na tela.
#     :param i: Inicio da contagem
#     :param f: Fim da contagem
#     :param p: Passo da contagem
#     :return: Sem retorno
#     Fução criada por Pedro Henrique
#     '''
#     c = i
#     while c <= f:
#         print(f'{c} ', end='')
#         c += p
#     print('FIM!')
#
#
# contador(2, 10, 2)
# help(contador)