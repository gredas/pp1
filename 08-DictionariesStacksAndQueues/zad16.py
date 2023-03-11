import json
f1 = open('students.json','r')
f2 = open('limited.json','w')
f3 = json.load(f1)
dictionary = {}
t = 0
for x in f3:
    for y,z in x.items():
        print(y,z)
        if t==0 or t==1 or t==2:
            dictionary[f'{y}']=f"{z}"
            t+=1
    t=0
    print(dictionary)
    json.dump(dictionary,f2,indent=4)
    f2.write('\n')