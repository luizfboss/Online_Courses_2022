def numero(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0


num = int(input('Number: '))


print(numero(num))
