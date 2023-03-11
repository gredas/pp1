
def f(dictionary,x,y):
    sum=0
    for k,q in dictionary.items():
        for w in q:
            if w>=x and w<=y:
                sum+=w
    return sum
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))