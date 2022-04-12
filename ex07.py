print(f'Entrada:\nCoordenadas de um ponto P(x, y)')
x = float(input('Digite o valor da coordenada X: '))
y = float(input('Digite o valor da coordenada Y: '))

if x > 0 and y > 0:
    r = 'o 1°'
elif x < 0 and y > 0:
    r = 'o 2°'
elif x < 0 and y < 0:
    r = 'o 3°'
elif x > 0 and y < 0:
    r = 'o 4°'
else:
    r = ' nenhum'
print(f'Saída:\nO ponto P({x}, {y}) pertence a{r} quadrante.')