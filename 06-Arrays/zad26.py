arr=[5,1,9,6,1]
large=0
max1=arr[0]
max2=arr[0]
for x in arr:
    for y in range(len(arr)):
        if x>=max1:
            max1=x
for x in arr:
    for y in range(len(arr)):
        if x<max1 and x>=max2:
            max2=x
print(max2)
