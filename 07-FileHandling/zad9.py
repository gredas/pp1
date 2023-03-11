f = open('numbers.txt','r')
sum = 0
for x in f:
    x = int(x)
    sum = sum + x
    print(sum)
f.close()