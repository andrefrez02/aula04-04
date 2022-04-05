'''Faça um programa em Python para uma loja de tintas. O programa deverá
pedir o tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
quantidades de latas de tinta a serem compradas e o preço total.
Obs: A quantidade de latas deverá ser um número inteiro. Utilize a função
math.ceil(x) da biblioteca math'''
import math
area = float(input('Entrada:\nDigite a área a ser pintada(em m²): '))
PRECO = 80.00

qlitros = area / 3
qlatas = qlitros / 18
qlatas = math.ceil(qlatas)

print(f'\nSaída:\nVocê precisará comprar {qlatas} lata(s)')
print(f'O valor total a pagar será de R${qlatas * PRECO:.2f}')