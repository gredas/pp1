def identity_matrix(n):
    
    
    arr=[]
    for x in range(0,n):
        arr.append([])
        for y in range(n):
            if y==x:
                arr[x].append(1)
            else:
                arr[x].append(0)
    return arr
print(identity_matrix(4))



