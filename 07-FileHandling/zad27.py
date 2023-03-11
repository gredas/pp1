import re
f1 = open('grades.txt','r')
f2 = f1.read()
#print(f2)
x = re.findall('\d.\d',f2)
#print(x)
t=0
sum=0
for y in x:
    y = float(y)
    sum+=y
    t+=1
print(sum/t)

