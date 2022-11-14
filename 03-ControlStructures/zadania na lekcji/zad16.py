x = input('enter first number\n')
y = input('enter second number\n')
try:
    if int(x) >= int(y):
        print(f' numbers {y} , {x}')
    else:
        print(f'numbers {x} , {y}')
except ValueError:
    print('podaj cyfre')
    