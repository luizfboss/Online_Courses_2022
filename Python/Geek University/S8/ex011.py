def notas(a, b, c):
    if c in 'Aa':
        return (a + b)/2
    elif c in 'Pp':
        return (a+b)/10
    else:
        return None


print(notas(3, 4, 'a'))
