'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

'''

#import math
from math import hypot
co = float(input('O comprimento do cateto oposto: '))
ca = float(input('O comprimento do cateto adjacente: '))
#hi = math.hypot(co, ca)
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
