nome = str(input('Qual é o seu nome? '))
if nome =='Pedro':
    print(f'Belo nome, {nome}!')
elif nome == 'Laura' or nome == 'junior' or nome == 'luis':
    print(f'Seu nome é bacana, {nome}!')
elif nome in 'Ana, Maria, Clara':
    print(f'Belo nome feminino, {nome}!')
else:
    print(f'Seu nome é comum, {nome}!')
print(f'Bom dia, {nome}!')