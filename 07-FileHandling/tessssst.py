x = input().split()
flag=True
arr1=[]
arr2=[]
if flag:
    rows=int(x[0])
    cols=int(x[1])
    flag=False
for q in range(rows):
    x2 = input().split()
    if flag==False:
        for y in x2:
            arr1.append(int(y))
        arr2.append(arr1)
        arr1=[]

arr2.reverse()
x2 = 5
#print(x2)
#x2=int(x2[0])
mini=999
minlist=0
minicolumn=0
t2=-1
for t in range(len(arr2)):
    for z in arr2:
        t2+=1
        if z[x2]<=mini:
            minlist=z
            minicolumn=t2
            mini=z[x2]
    arr1.append(minlist)
    del arr2[minicolumn]
    t2=-1
    mini=999
for w in arr1:
    for o in w:
        print(o,end=' ')
    print()

