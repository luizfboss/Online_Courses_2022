import math


def pitagoras(a, b):
    h = math.sqrt(a**2 + b**2)
    return h


co = float(input('Co: '))
ca = float(input('Ca: '))
print(f'Hypot value: {pitagoras(co, ca)}')
