galera = list()
dados = list()
totmai = totmen = 0
for c in range(0,3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'temos {totmai} maiores de idade e {totmen} menores de idade')








# galera = [['João', 19], ['Ana', 33],['Joaquim', 13], ['Maria', 45]]
#
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')
# teste = list()
# teste. append('gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = '22'
# galera.append(teste[:])
# print(galera)