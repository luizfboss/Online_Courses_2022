import math


def tangente(a):
    return math.sinh(math.radians(a))


angulo = int(input('Angulo: '))
print(tangente(int(input('Angulo: '))))
