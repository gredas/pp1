f1 = open('meatandfish.txt','r')
f2 = open('GrainsAndBread.txt','r')
f3 = open('shoppinglist.txt','w')
for x in f1:
    f3.write(x)
f3.write('\n')
for y in f2:
    f3.write(y)
f1.close()
f2.close()
f3.close()