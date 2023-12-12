c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32   #9 * c / 5 + 32 nesse contexto não precisaria de (), a ordem de precência se mantém.
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(c, f))