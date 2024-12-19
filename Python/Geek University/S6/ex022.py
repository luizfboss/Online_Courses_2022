notas = list()

while True:
    a = float(input('Grade: '))
    notas.append(a)
    print('-'*20)
    if 10 > a or a > 20:
        break
print(f'Average: {sum(notas)/len(notas):.2f}')
