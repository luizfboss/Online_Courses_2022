import math


def volume_da_esfera(raio):
    return f'O volume da esfera foi de {v:.2f}cm3'


r = int(input('Radius (centimeters): '))
v = (4 * math.pi * (r**3))/3
print(volume_da_esfera(r))
