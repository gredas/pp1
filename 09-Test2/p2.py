def f(human_age):
    t=0
    dog=0
    while t!=human_age:
        if t==0 or t==1:
            dog+=10
        else:
            dog+=4
        t+=1
    return dog
print(f(4))

