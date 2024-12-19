import math


def cosseno(a):
    return math.cos(math.radians(a))


angulo = int(input('Angulo: '))
print(cosseno(angulo))
