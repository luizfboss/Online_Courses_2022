num = int(input('Number: '))
resto = 1000 - num
num += resto
while num < 100000:
    num += 1000
    if num >= 101000:
        num = 100000
        break
    print(num, end=' ')
