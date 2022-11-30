arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
arr2=[]
print(arr)
tick1=0
tick2=0
x1=None
for x in arr:
    for y in x:
        if tick1==0:
            x1=arr[tick2][0]
            arr[tick2][0]=arr[tick2][-1]
            arr[tick2][-1]=x1
        tick1+=1
    tick2+=1
    tick1=0
print(arr)

