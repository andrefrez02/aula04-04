num = int(input('Entrada: \nDigite um número inteiro: '))
if num > 0: txt = 'é positivo.'
elif num < 0: txt = 'é negativo.'
else: txt = 'é nulo.'
print(f'\nSaída: \nO número {num} {txt}')