import re
x = open('shoppinglist.txt','r')
z = x.read()
#print(z)
findall=re.findall('\w{6,}',z)
#print(findall)
for aaa in findall:
    print(aaa)
