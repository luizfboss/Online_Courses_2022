escolha = str(input('ESCOLHA UM OPERADOR: +, -, /, *: ')).strip()
a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
if escolha == '+' or '-' or '*' or '/':
    if escolha == '+':
        resultado = a+b
        print(f'Resultado de {a}+{b}:', a+b)
    elif escolha == '-':
        resultado = a-b
        print(f'Resultado de {a}-{b}:', a-b)
    elif escolha == '/':
        resultado = a/b
        print(f'Resultado de {a}/{b}:', a/b)
    elif escolha == '-':
        resultado = a*b
        print(f'Resultado de {a}*{b}:', a*b)
    else:
        print('Erro. Escolha um valor valido.')
