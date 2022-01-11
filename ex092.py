from datetime import  datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')





















# a = datetime.today().year
# pessoas = {'nome': '', 'idade': '', 'ctps': '', 'contratação': '', 'salario': '', 'aposentadoria': ''}
#
# pessoas['nome'] = str(input('Nome: '))
# ano = int(input('Ano de Nascimento: '))
# pessoas['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
# pessoas['idade'] = a - ano
# if pessoas['ctps'] != 0:
#     pessoas['contratação'] = int(input('Ano de contratação: '))
#     pessoas['salario'] = float(input('Saláio: R$ '))
#
#     print('-=' * 30)
#     print(f'Nome tem o valor {pessoas["nome"]}')
# print(f'Idade tem o valor {pessoas["idade"]}')
# if pessoas['ctps'] != 0:
#     print(f'CTPS tem o valor {pessoas["ctps"]}')
#     print(f'Contratação tem o valor {pessoas["contratação"]}')
#     print(f'Salário tem o valor R${pessoas["salario"]:.2f}')
#     print(f'Aposentadoria tem o valor')
#     c = pessoas['contratação'] - ano
#     print(f'Aposentadoria tem o valor {c+35}')
# else:
#     print('CTPS tem o valor 0')