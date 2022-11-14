n = int(input('podaj liczbe: '))
flag = False
if n == 1:
    flag = False
elif n == 2:
    flag = True
else:
    for x in range(2,n):
        y = n%x
        if y == 0:
            flag = False
            break
        else:
            flag = True
if flag:
    print('prime')
else:
    print('not prime')
        


