
def create_2d_arr(x,y):
    arr = []
    for f in range(y):
        arr.append([])
        for z in range(x):
            arr[f].append(0)
    return arr
        
print(create_2d_arr(3,4))
