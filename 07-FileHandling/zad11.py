x = ['a','b','c','d','f']
y = open('1titles.txt','w')
for z in x:
    y.write(f'{z}\n')
y.close()

