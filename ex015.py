dias = int(input('Por quantos dias foi alugado?'))
km = float(input('Quantos KM percorridos?'))

pago = (dias*60)+(km*0.15)

print(f'Total a pagar R${pago:.2f}')