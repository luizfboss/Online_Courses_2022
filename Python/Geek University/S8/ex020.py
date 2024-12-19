def fatorial(a):
    fator = 1
    for c in range(a, 0, -1):
        fator *= c
    return fator


print(fatorial(4))
