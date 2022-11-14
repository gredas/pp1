try:
    x = int(input('dog age\n'))
    if x == 1:
        print('human age is 10.5')
    elif x >= 2:
        x = x - 2
        x = x * 4 + 21
        print(f'human age is {x}')
    else:
        print('enter correct value')
except ValueError:
    print('wrong value')