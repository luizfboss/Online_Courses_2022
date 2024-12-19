soma = 0

a = int(input('Number: '))
for c in range(2, a):
    if a % c == 0:
        soma += c
        print(f'{c}  is multiple of {a}')
print(f'Sum of all multiples of {a}: {soma}')
