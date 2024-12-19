n = int(input('Number: '))
if n % 2 == 0:
    for c in range(n+1, 1, -1):
        if c % 2 == 0:
            print(c)
