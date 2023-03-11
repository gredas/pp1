with open('numbers1.txt','w') as f:
    for x in range(1,51):
        x = str(x)
        f.write(f'{x}\n')