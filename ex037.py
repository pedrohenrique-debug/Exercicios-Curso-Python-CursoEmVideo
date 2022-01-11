numero = int(input('Digite um numero que deseja converter: '))

print('1: para binario')
print('2: para octal')
print('3: para hexadecimal')
num2 = int(input('Digite a opção desejada? '))

if num2 == 1:

    print(f'{numero} em binário é {int(bin(numero)[2:])}')
elif num2 ==2:
    print(f'{numero} em octal é {oct(numero)[2:]}')
elif num2 == 3:
    print(f'{numero} em hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')