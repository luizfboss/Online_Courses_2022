num = int(input('Number: '))
if num % 3 == 0:
    print(f'The number {num} is divisible by 3')
if num % 3 != 0:
    print(f'The number {num} is not divisible by 3')
if num % 5 == 0:
    print(f'The number {num} is divisible by 5')
if num % 5 != 0:
    print(f'The number {num} is not divisible by 5')
elif num % 5 != 0 and num % 3 != 0:
    print('Esse numero nao pode ser dividido por 3 e 5')