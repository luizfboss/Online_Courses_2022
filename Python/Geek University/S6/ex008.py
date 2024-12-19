maior = 0
menor = 0

for c in range(10):
    num = int(input('Number: '))
    if num < menor:
        menor = num
    elif num > maior:
        maior = num
print(f'Smalest: {menor}')
print(f'Greatest: {maior}')
