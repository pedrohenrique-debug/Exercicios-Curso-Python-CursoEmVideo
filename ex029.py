
vel = int(input('Qual a velocidade em Km/h? '))
m = (vel - 80)*7
n = vel-80
if vel > 80:
    print(f'Você passou {n}Km/h acima do limite de velocidade.')
    print(f'Você foi multado em {m:.2f} reais!')

print('Tenha um bom dia! Dirija com segurança!')
