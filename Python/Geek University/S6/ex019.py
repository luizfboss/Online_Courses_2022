a = (int(input('insira um numero entre 100 e 999: ')))
if a < 100 or a > 999:
    a = (int(input('insira um numero entre 100 e 999')))
    if 100 < a > 999:
        print('Digite um numero valido. ')
b = str(a)
for i, v in enumerate(b):
    print(v)
