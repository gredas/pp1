arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]
sum='Niepowtarzajace sie:'
for x in arr1:
    for y in arr2:
        if x==y:
            flag=False
            break
        else:
            flag=True
    if flag==True:
        sum=sum+' '+str(x)
    
print(sum)