def soma_algarismos():
    n = int(input("Digite um número inteiro: "))
    soma = 0
    while n > 0:
        resto = n % 10
        n = (n - resto) / 10
        soma = soma + resto
    return n


print(soma_algarismos())