c = 1
with open('teste.txt', 'r') as arquivo:
    for letras in arquivo.read():
        if letras in 'aeiou':
            c += 1
    print(c)
