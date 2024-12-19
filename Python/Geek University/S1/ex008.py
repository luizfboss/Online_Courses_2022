a = float(input('Primeira nota: '))
if a > 10:
    print('Nota invalida por ser maior que 10.00. Tente novamente.')
    quit()
elif a < 0:
    print('Nota invalida por ser menor que 0. Tente novamente.')
    quit()

b = float(input('Segunda nota: '))
if b > 10:
    print('Nota invalida por ser maior que 10.00. Tente novamente.')
    quit()
elif b < 0:
    print('Nota invalida por ser menor do que 0. Tente novamente.')
    quit()
if 0 < a < 10 and 0 < b < 10:
    condicao = 'reprovado'
    media = (a + b) / 2
    print(f'Media das notas: {media}')
    if media >= 5:
        condicao = 'APROVADO'
        print(f'Condicao do aluno: {condicao}')
    if media < 5:
        condicao = 'REPROVADO'
        print(f'Condicao do aluno: {condicao}')
else:
    print('Erro. Nota acima de 10.0 ou abaixo de 0.00.'
          'Tente Novamente.')
