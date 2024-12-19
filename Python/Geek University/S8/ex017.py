def somas(a, b):
    soma = 0
    for c in range(a-b, a+1):
        soma += c
    return soma


print(somas(10, 6))
