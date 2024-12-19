nota1 = float(input('First grade: '))
nota2 = float(input('Second grade: '))
nota3 = float(input('Third grade: '))
media = (nota1 + nota2 + (2*nota3))/3
print(f'Average: {media:.2f}')
if media >= 6:
    print('Situation: APPROVED.')
else:
    print('Situation: REPROVED')
