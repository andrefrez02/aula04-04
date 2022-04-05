compra = float(input('Digite o valor da compra: '))
parc = int(input('Digite a quantidade de parcelas: '))

match(parc):
    case 2: valor = compra * 1.03
    case 4: valor = compra * 1.07
    case 6: valor = compra * 1.09
    case 8: valor = compra * 1.12
    case _: valor = 0
if valor == 0:
    print('Parcelamento inválido!!!')
else:
    print(f'Parcela = {valor/parc}')
