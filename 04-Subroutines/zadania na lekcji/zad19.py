def in_range(n,x,y):
    flag = None
    if n>=x and n<=y:
        flag = True
    else:
        flag = False
    return flag
print(in_range(4,5,6))
