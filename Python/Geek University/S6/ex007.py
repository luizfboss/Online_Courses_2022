total = 0
for c in range(10):
    num = int(input('Number: '))
    print('-'*20)
    if num >= 0:
        total += num
print(f'Avg: {total/10}')
