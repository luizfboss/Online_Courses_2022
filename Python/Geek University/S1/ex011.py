soma = 0
number = str(input('Number: '))
numero1 = int(number)
if numero1 > 0:
    for numero in number:
        algarismo = int(numero)
        soma += algarismo
    print(f'Sum of all numbers: {soma}')
else:
    print('Invalid number.')
