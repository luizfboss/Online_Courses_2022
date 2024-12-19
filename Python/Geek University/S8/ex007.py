def conversor_farenheit(c):
    f = c * (9/5) + 32
    return f


a = float(input('Temperature (Celcius): '))
print(f'{conversor_farenheit(a):.1f}')
