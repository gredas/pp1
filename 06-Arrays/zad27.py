arr=[5,1,9,6,1]
max=arr[0]
min=arr[0]
for x in arr:
    if x>=max:
        max=x
for x in arr:
    if x<=min:
        min=x
print(max-min)
    
