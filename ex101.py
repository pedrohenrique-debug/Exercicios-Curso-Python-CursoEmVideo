import datetime
def voto(ano):
    '''
    Calcula a idade e informa se não pode, é opcional ou é obrigatorio votar
    :param ano: ano que o usuario digitou
    :return: o valor que a função voto() retorna
    '''
    idade = datetime.datetime.now().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade <= 16:
        return 'Não pode votar ainda.'
    if idade < 18 or idade > 65:
        return 'Voto opcional.'
    else:
        return 'Voto obrigatorio.'


print('-' * 20)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
