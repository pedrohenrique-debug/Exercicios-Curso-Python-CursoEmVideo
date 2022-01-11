print('-='*20)
valor = float(input('Qual o valor da casa? '))
print('-='*20)
salario = float(input('Qual o salário?'))
print('-='*20)
anos = int(input('Quantos anos? '))
print('-='*20)

parcela = (valor / anos) / 12
p = salario * 0.30
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos')
print(f'a prestação será de R${parcela:.2f}')
if parcela > p:
    print('\033[1;91mNão é possivel realizar o emprestimo!\033[m')
else:
    print('\033[1;32mÉ possivel realizar o emprestimo\033[m')
print('-='*20)
print('Tenha um bom dia!')