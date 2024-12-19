salario = float(input('Salario: '))
prestacao = float(input('Prestacao do emprestimo: '))
if prestacao > 0.2*salario:
    print('Emprestimo nao concedido')
else:
    print('Emprestimo concedido')