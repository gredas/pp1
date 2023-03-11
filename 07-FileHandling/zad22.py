import csv
with open('students.csv','r') as x:
    s = csv.reader(x)
    t = 0
    for row in s:
        if t == 0:
            t+=1
        else:
            row[2]=int(row[2])
            if row[2]<30:
                print(row[0],end=' ')
                print(row[1],end=' ')
                print(row[-1],end=' ')
                print()
