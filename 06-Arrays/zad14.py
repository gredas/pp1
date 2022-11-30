arr = [[True,False],[True,True],[False,False]]
for x in arr:
    if x[0]==True:
        x[0]=False
    else:
        x[0]=True
    if x[1]==True:
        x[1]=False
    else:
        x[1]=True
print(arr)
    