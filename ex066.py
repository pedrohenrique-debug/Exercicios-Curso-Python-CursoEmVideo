soma = quant = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'A soma dos {quant} valores foi {soma}')
print('FIM')