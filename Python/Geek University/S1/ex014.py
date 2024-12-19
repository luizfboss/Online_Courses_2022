lab = float(input("Laboratory grade: "))
semestral = float(input("Semestral grade: "))
final = float(input("Final exam's grade: "))
if 10 > lab >= 0 and 10 > semestral >= 0 and 10 > final >= 0:
    media = ((lab*2) + (semestral*3) + (final*5)) / 10
    print(f'Media: {media}')
    if 0 < media < 2.9:
        print('Situacao: REPROVADO')
    elif 3 < media < 4.9:
        print('Situacao: RECUPERACAO')
    elif media >= 5:
        print('Situacao: APROVADO')
    else:
        print('Erro')
else:
    print('Erro. Insira uma nota valida')
