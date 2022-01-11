print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO')


    if r1 == r2 and r2 == r3:
        print('pode formar um triângulo equilátero')
    elif r1 == r2 and r2 != r3 or r1 == r3 and r1 != r2:
         print('Pode formar um triângulo isósceles')
    else:
         print('Pode formar triângulo escaleno')
else:
    print('Não podem formar um triângulo')
