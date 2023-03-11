import re
m = 'To be, or not to be, that is the question'
x = re.findall('[aeiouyAEIOUY]',m)
t = 0
for z in x:
    t+=1
print(t)
print(x)