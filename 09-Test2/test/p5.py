import csv
def f(name,surname):
    f1 = open('C:\\Users\\bartl\\OneDrive\\Pulpit\\python\\pp1\\09-Test2\\test\\data.csv','r')
    f2 = csv.reader(f1)
    flag=False
    for x in f2:
        print(x)
        if x[0]==name:
            if x[1]==surname:
                exp=x[-3]
                salary=x[-5]
                print(salary)
                print(exp)
                if exp*2>=salary:
                    flag=True
                else:
                    flag=False
    f1.close()
    return flag
print(f("Evie","Klampt"))