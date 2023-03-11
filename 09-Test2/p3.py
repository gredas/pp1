def f(array2d):
    arr = []
    s = 0
    for x in range(len(array2d[0])):
        for y in array2d:
            s+=y[x]
        arr.append(s)
        s=0
    return arr
print(f([[3,6,2,7],[9,5,4,0],[2,8,0,9]]))