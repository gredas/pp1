arr = [-15,8,-31,47,-2,19]
min = arr[0]
max = arr[0]
for x in arr:
    if x <= min:
        min = x
    elif x >= max:
        max = x
print(min,max)