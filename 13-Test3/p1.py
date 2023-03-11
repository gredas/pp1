def f(n):
    string = ''
    for x in range(1,n+1):
        if x%5==0 and x!=1 and x!=n:
            string = string + '/-'
        else:
            string = string + '/'
    return string
print(f(11))
            