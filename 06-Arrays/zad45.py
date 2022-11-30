def two_dimensional(n):
    arr = []
    for x in n:
        for y in x:
            arr.append(y)
    return arr
print(two_dimensional([[2,3],[1,5]]))
