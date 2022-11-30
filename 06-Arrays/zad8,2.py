arr = [-15,8,-31,47,-2,19]
min = arr[0]
max = arr[0]
for x in arr:
    if x >= max:
        max = x
    elif x <= min:
        min = x
print(min)
print(max)
