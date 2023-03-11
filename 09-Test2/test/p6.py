import json
def f(name,surame):
    f1 = open('data.json','r')
    f2 = json.load(f1)
    str=""
    t=0
    for x in f2:
        if x["name"]==name:
            if x["surname"]==surame:
                l = x["languages"]
                for ld in l:
                    if t==len(l)-1:
                        str=str+ld
                        t+=1
                    else:
                        str=str+ld+','
                        t+=1
        t=0
        f1.close()
    return str


    

