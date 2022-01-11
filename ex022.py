'''nome = str(input('Qual seu nome completo?')).strip()

maiusculas = nome.upper()
minusculas = nome.lower()
divisão = nome.split()
letras = ''.join(divisão)
b = len(letras)
primeiro = divisão[0]
c = len(primeiro)
print(f'Analisando seu nome...\nSeu nome em maiúsculas: {maiusculas} \nSeu nome em minúsculas: {minusculas}\nSeu nome tewm ao todo {b} letras \nSeu primeiro nome é {primeiro} e ele tem {c} letras')'''

nome= str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")}')
#print(f'Seu primeiro nome tem {nome.find(" ")}')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
