import re
m = 'To be, or not to be, that is the question'
z=re.sub(',','',m)
x = re.split('\s',z)
print(x)
tick=0
for t in x:
    tick+=1
print(tick)