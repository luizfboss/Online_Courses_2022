import math
a = int(input('First Number: '))
if a > 0:
    print(f'Square root of {a}: {math.sqrt(a):.2f}')
elif a < 0:
    print('Invalid number. Try again.')
else:
    print('Numero = 0. Try another one.')
