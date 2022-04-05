print('Entrada:')
sal = float(input('Digite o valor do teu salário fixo: R$'))
ven = float(input('Digite o valor das tuas vendas: R$'))

print('\nSaída:')
print(f'Comissão: {0.04 * ven:.2f}')
print(f'Salário final: {sal + (ven * 0.04):.2f}')