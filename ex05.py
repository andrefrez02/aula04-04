import math
area = float(input('Entrada:\nDigite a área a ser pintada(em m²): '))
PRECO = 80.00

qlitros = area / 3
qlatas = qlitros / 18
qlatas = math.ceil(qlatas)

print(f'\nSaída:\nVocê precisará comprar {qlatas} lata(s)')
print(f'O valor total a pagar será de R${qlatas * PRECO:.2f}')