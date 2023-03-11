import json
def f(age,course,average):
    f1 = open('test.json','r')
    f2 = json.load(f1)
    sum=0
    t=0
    c=0
    for x in f2:
        if x["age"]>=age:
            for z in x["studies"]["courses"]:
                if z["name"]==course:
                    for q in z["grades"]:
                        sum+=q
                        t+=1
                    if (sum/t)>=average:
                        c+=1
                        sum=0
                        t=0
    return c
print(f(21, "statistics", 3))  
            

