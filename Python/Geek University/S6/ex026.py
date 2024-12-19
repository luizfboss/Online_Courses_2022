a = int(input('Number: '))
count = a

while True:
    count += 1
    if count % 11 == 0:
        print(f'The first multiple of 11 is {count} '
              f'and its division by 11 is {count/11:.0f}.')
        break
    elif count % 13 == 0:
        print(f'The first multiple of 13 is {count} '
              f'and its division by 13 is {count/13:.0f}.')
        break
    elif count % 17 == 0:
        print(f'The first multiple of 17 is {count} '
              f'and its division by 17 is {count/17:.0f}.')
        break
