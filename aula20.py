def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)

# def dobra(lst):
#     pos=0
#     while pos < len(lst):
#         lst[pos]*=2
#         pos+=1
# valores = [7, 2, 5, 0, 4]
# dobra(valores)
# print(valores)

# def contador(* num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números')
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)
# for valor in num:
#     print(f'{valor} ', end='')
# print('FIM!')

# def soma(a, b):
#     print(f'A vale {a} B vale {b}')
#
#     s = a + b
#     print(f'A soma de A + B é {s}')
# #Programa Principal
# soma(5, 4)




# def mensagem(msg):
#     print('-' * 30)
#     print(msg)
#     print('-' * 30)
#
# mensagem('Ola mundo')
