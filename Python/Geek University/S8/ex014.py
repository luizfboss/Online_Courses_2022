def quilometros_litro(a, b):
    kml = a / b
    if kml < 8:
        return 'Venda o carro!'
    elif 8 < kml < 14:
        return 'Economico'
    elif kml > 12:
        return 'Super economico'


quilometros = int(input('Quilometros: '))
litros = int(input('Litros: '))
print(quilometros_litro(quilometros, litros))
