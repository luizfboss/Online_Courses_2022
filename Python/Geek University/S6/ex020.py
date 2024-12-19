lista = list()
listapar = list()


while True:
    a = int(input('Number (Type 1000 to break): '))
    lista.append(a)
    if a % 2 == 0:
        listapar.append(a)
    if a >= 1000:
        break
print(f'Amount of numbers written: {len(lista)}')
print(f'Amount of evens: {len(listapar)}')
