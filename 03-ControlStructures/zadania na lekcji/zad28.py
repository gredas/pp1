a = 0
b = 1
c = None
print(a, end=" ")
print(b, end=" ")
for x in range(1,13):
    c = a + b
    print(c, end=" ")
    a = b 
    b = c
