import math


def volume_do_cilindro(a, b):
    v = math.pi * (b**2) * a
    return v


h = float(input('H (cm): '))
r = float(input('Radius(cm): '))
print(f'{volume_do_cilindro(h, r):.1f}cm3')
