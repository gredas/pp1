arr = [1,2,3,4,5,6,7]
x = 0
even = 0
odd = 0
while len(arr) != x:
    if x%2==0:
        odd+=1
        x+=1
    else:
        even+=1
        x+=1
print(odd,even)
