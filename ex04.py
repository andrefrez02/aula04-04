alt = float(input('Entrada:\nDigite a altura da pessoa em metros: '))
gen = str(input('Digite o sexo da pessoa(m/f): '))

if gen in 'mM':
    peso = (72.7 * alt) - 58
elif gen in 'fF':
    peso = (62.1 * alt) - 44.7
else:
    print('Digite apenas "M" ou "F".')
    peso = 0

print(f'\nSaída:\nO peso ideal dessa pessoa é {peso:.2f}KG')