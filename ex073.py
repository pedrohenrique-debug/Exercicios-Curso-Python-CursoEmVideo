time =  ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense','América-MG','Atlético-GO','Santos','Ceará','Internacional'
,'São Paulo'
,'Athletico-PR'
,'Cuiabá'
,'Juventude'
,'Grêmio'
,'Bahia'
,'Sport'
, 'Chapecoense')
print('-='*15)
print(f'Lista de times do Brasileirão: {time}')
print('-='*15)
print(f'Os 5 primeiros são {time[:5]}')
print('-='*15)
print(f'Os 4 ultimos são {time[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-='*15)
print(f'O {time[19]} está na {time.index("Chapecoense")+1}ª posição')
print('-='*15)


