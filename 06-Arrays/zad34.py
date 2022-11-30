arr1 = [1,2,3,4]
arr2 = [1,1,2,3,4]
z = 0
for x in arr1:
    for y  in arr2:
        if x == y:
            z += 1
            break
if z == len(arr1):
    print('ta')
else:
    print('nie')

