def median(arr):
    help=0
    for x in arr:
        for y in range(len(arr)-1):
            if arr[y]>=arr[y+1]:
                help=arr[y]
                arr[y]=arr[y+1]
                arr[y+1]=help
    print(arr)            

    if len(arr)%2==1:
        x=arr[len(arr)//2]
        print(f'median: {x}')
    else:
        x=((arr[(len(arr)//2)-1])+arr[len(arr)//2])/2
        print(f'median: {x}')
        
median([1,0,9,4,6])