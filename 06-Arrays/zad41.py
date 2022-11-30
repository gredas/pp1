arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
arr2=[]
print(arr)
x = arr[0]
y = arr[-1]
tick=1
arr2.append(arr[-1])
for x in arr:
    if tick==1 or tick==len(arr):
        tick+=1
    else:
        arr2.append(x)
        tick+=1
arr2.append(arr[0])
print(arr2)

