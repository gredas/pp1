def minmax(arr):
    min = arr[0]
    max = arr[0]
    for x in arr:
        if x>=max:
            max=x
    for x in arr:
        if x<=min:
            min=x
    return [max,min]
    
arr = [4,2,8,4,7,9,5]
print(minmax(arr))
