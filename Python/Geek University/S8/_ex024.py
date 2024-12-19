def piramide(a):
    base = (2*a) - 1
    metade = base/2
    for c in range(1, base, 2):
        print('*' * c)
    return ' '


print(piramide(6))
