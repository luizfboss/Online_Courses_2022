menor = float(input('Menor base: '))
maior = float(input('Maior base: '))
altura = float(input('Altura: '))
if menor < 0 or maior < 0:
    print('Erro. Selecione um numero valido (maior que 0.)')
    quit()
area = ((menor + maior) * altura) / 2
print(f'Area do trapezio: {area}')
