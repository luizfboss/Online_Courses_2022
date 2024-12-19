a = int(input('First number: '))
b = int(input('Second number: '))
if a < b:
    print(f'Greatest number: {b}')
    print(b-a)
elif a > b:
    print(f'Greatest number: {a}')
    print(a-b)
else:
    print('They are equal')
