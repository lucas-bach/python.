#import math - Aqui ele importa a biblioteca inteira.
from math import sqrt # aqui importa apenas uma funcionalidade, no caso raiz quadrada.
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
