def bubblesort(arr):
    z=0
    arrrrr=len(arr)-1
    for x in arr:
        for y in range(arrrrr):
            if arr[y]>=arr[y+1]:
                z = arr[y]
                arr[y]=arr[y+1]
                arr[y+1]=z
    print(arr)
bubblesort([2,4,2,5,75,4,53,1])
