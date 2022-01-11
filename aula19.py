estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()










# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# pessoas['peso'] = 98.5
# # pessoas['nome'] = 'Leandro'
# # del pessoas['sexo']
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
#

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')