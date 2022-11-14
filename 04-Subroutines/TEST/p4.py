def f(number, even):    
    number = str(number)
    sum = 0
    for n in number:
        n = int(n)
        if even == True:
            if n%2 == 0:
                sum = sum + int(n)
        else:
            if n%2 == 1:
                sum = sum + int(n)
    return sum
print(f(20576,True))