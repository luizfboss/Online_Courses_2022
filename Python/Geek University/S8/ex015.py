def triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return 'Triangulo Equilatero'
        if a == b != c or b == c != a or a == c != b:
            return 'Triangulo Isoceles'
        if a != b != c:
            return 'Triangulo Escaleno'
        else:
            return None
    else:
        return 'Lados incompativeis para ser um triangulo'


print(triangulo(2, 3, 6))