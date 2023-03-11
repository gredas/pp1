x = input('File name: ')
y = open(f'{x}','r')
sum = 0
for z in y:
    sum += 1
print(f'Number of lines: {sum}')
y.close()
x.close()

