s = str(input('Gender [M/W]: ')).upper().strip()
h = float(input('Insert your height: '))
if s == 'M':
    peso_ideal = (72.7 * h) - 58
    print(peso_ideal)
elif s == 'W':
    peso_ideal = (62.1*h) - 44.7
    print(peso_ideal)
else:
    print('Selecione uma opcao valida.')
