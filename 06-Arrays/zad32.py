arr = [5,4,3,5,2,6,5]
a = ''
y = 1
for x in arr:
    if y == len(arr) :
        a = a + str(x)
    else:
        a = a + str(x) + ","
        y += 1

print(a)
