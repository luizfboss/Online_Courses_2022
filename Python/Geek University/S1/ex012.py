import math
num = float(input('Number: '))
if num > 0:
    print(f'Full number: {math.log(num)}')
    print(f'Log({num}) abreviated: {math.log(num):.2f}')
else:
    print('Invalid number. Try again.')
