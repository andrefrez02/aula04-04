nome = input('Entrada:\nQual o seu nome?: ')
hora = int(input('Que horas são[0-23h]?:'))

if hora > 4 and hora < 13:
    r = 'Bom dia '
elif hora > 12 and hora < 18:
    r = 'Boa tarde '
else:
    r = 'Boa noite '

print(f'Saída\n{r}{nome}')