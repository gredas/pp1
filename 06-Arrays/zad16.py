arr = [15,8,31,47,2,19]
print(arr)
y = -1
x = 0
last=0
for z in range(len(arr)//2):
    last=arr[y]
    arr[y]=arr[x]
    arr[x]=last
    x+=1
    y+=-1
print(arr)


