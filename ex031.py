dis = float(input(('Qual a distância em Km/h? ')))

if dis <= 200:
    print(f'A viagem custou R${dis*0.50:.2f}')
else:
    print(f'A viagem custou R${dis*0.45:.2f}')

#foma alternativa
#precço = distância * 0.50 if distência <= 200 else distância * 0.45