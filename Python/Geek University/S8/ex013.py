def calculo(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '/':
        return a / b
    elif c == '*':
        return a * b
    else:
        return None


print(calculo(3, 5, '+'))
