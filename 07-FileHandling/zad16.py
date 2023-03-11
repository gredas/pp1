x = open('numbers.txt','r')
y = open('copy.txt','w')
for z in x:
    y.write(z)
y.close()
x.close()