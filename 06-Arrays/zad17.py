arr = [8,2,5,1,9]
y=0
for x in arr:
    arr[y]=arr[y]**2
    y+=1
print(arr)