arr = [[-38, 19], [5,40],[-70,110],[29,16]]
rowmax=1
columnmax=1
rowmin=1
columnmin=1
d = 1
c = 1
max=arr[0][0]
min=arr[0][0]
for x in arr:
    for y in x:
        if y>=max:
            max = y
            rowmax=c
            columnmax=d
        if y<=min:
            min = y
            rowmin=c
            columnmin=d
        d +=1
    d=1
    c+=1
print(columnmax,rowmax,max)
print(columnmin,rowmin,min)
       
    
        