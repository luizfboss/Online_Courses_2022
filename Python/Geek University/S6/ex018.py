lista = list()

while True:
    a = input('Number: ')
    if a.isnumeric():
        lista.append(a)
    else:
        break
maior = max(lista)
print(f'Greatest number: {maior}')
print(f'Amount of times {maior} is in list: {lista.count(maior)}')
