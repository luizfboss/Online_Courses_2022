import math


def tangente(a):
    return math.cosh((math.radians(a)))


angulo = int(input('Angulo: '))
print(tangente(int(input('Angulo: '))))
