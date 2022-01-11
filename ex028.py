import random
from time import sleep
print(f'-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-'*20)

num = int(input('Em qual numero pensei?'))

m = random.randint(0, 5)
print('PROCESSANDO...')
sleep(3)
if num == m:
    print('Você venceu!')
else:
    print(f'GANHEI! Eu pensei no numero {m} e não no {num}!')

print('FIM!')

