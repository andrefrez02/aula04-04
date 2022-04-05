n1 = float(input('Entrada:\nDigite a primeira nota parcial: '))
n2 = float(input('Digite a segunda nota parcial: '))
med = (n1 + n2)/2
print(med)
if med >= 9.0:
    con = 'A'
    men = 'APROVADO!'
elif med >= 7.5:
    con = 'B'
    men = 'APROVADO!'
elif med >= 6:
    con = 'C'
    men = 'APROVADO!'
elif med >= 4:
    con = 'D'
    men = 'REPROVADO!'
else:    
    con = 'E'
    men = 'REPROVADO!'
if con in 'ABC':
    men = 'APROVADO!'
else:
    men = 'REPROVADO!'
print(f'\nSaída\nConceito: {con}')
print(f'Mensagem: {men}')