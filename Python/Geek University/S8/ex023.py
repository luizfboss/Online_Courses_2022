def piramide(a):
    for c in range(a):
        print('*' * c)
    for c in range(a, 0, -1):
        print('*' * c)
    return ' '


print(piramide(7))
