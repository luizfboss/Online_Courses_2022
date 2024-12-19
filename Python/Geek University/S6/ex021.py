pares = 0
impares = 1

a = int(input('First number: '))
b = int(input('Second number: '))
for c in range(a, b+1):
    if c % 2 == 0:
        pares += c
    if c % 2 == 1:
        impares *= c

print(f'Sum of all evens: {pares}')
print(f'Product of all odds: {impares}')
