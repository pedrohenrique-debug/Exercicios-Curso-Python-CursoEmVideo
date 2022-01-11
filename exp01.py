setora = 2000
setorb = 1000
email = ['rique']
senha = ['12345']
usuario = []
v = 0
print('-' * 30)
print(f'{"BANCO INTERNO":^30}')
print('-' * 30)
print(f'{"SELECIONE COMO DESEJA ENTRAR":^30}')
print('''[1] ADMIN
[2] USUARIO
[3] SAIR''')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:

    admin = str(input('SEU NOME DE USUARIO: '))
    adminsenha = str(input('SUA SENHA: '))
    if admin in email and adminsenha in senha:
        v = 0
        print('''[1] ADICIONAR USUARIO
[2] AUMENTO 
[3] CORTE DE SALARIO
[4] PAGAMENTOS JÁ RETIRADOS
[5] SAIR''')
    else:
        print('USUARIO OU SENHA INVALIDO. TENTE NOVAMENTE...')
if


