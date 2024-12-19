soma = 0

for c in range(1, 1000):
    if c % 5 == 0:
        soma += c
    if c % 3 == 0:
        soma += c
print(soma)
