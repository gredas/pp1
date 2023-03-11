with open('numbers123.txt','w') as x:
    for y in range(1,11):
        x.write(f'{y},{y**2},{y**3}\n')