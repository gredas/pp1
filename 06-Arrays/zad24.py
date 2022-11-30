arr = [2,3,2,5,8,1,9,8]
unique=0
sum='Unique elements: '
for x in arr:
    for y in range(len(arr)):
        if x==arr[y]:
            unique+=1
    if unique==1:
        sum=sum+str(x)+' '
    unique=0
print(sum)

