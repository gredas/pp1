arr = ['Genowefa','Onufry','Celestyna','Alojzy', 'Pankracy']
x = 0
for y in range(len(arr)):
    if len(arr[y]) >= x:
        x = len(arr[y])
        z = arr[y]
print('names:',end=' ')
for r in arr:
    print(r,end=" ")
print()
print(f'longest name: {z}')
