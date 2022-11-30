def transpose_matrix(m):
    arr = []
    t=0
    for z in range(len(m[0])):
        arr.append([])
    for x in m:
        for y in x:
            arr[t].append(y)
            t+=1
        t=0
    return arr
print(transpose_matrix([[1,2,3,4,5],[6,7,8,9,10]]))


