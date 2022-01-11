num = cont = soma = 0
num = int(input('Digite um número [999 para parar]'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]'))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')












'''cont = 0
n = []
while not 999 in n:
    n.append(int(input('Digite um numero ')))

    cont += 1
a = sum(n)
b = n.pop()
print(f'Você digitou {cont-1} numeros e a soma deles é {a-b}')

'''