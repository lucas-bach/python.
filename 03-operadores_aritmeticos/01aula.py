n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dr = n1 % n2
e = n1 ** n2
print('A soma vale {}, o produto é {} e a divisão é {:.2f}' .format(s, m, d))
print('Divisão inteira {}, o resto da divisão é {} e a potência é {}' .format(di, dr, e))