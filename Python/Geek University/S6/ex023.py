a = int(input('Number: '))
for c in range(2, a):
    if a % c == 0:
        print(f'{c}  is multiple of {a}')
