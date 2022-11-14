a = int(3)
b = int(1)
if a == 0 or b == 0:
    print(" ")
elif a == 1 and b != 0:
    print("*"*b)
elif a!=0 and b == 1:
    for x in range(1,a+1):
        print("*")
elif a > 1 and b != 0:
    print ("*"*b)
    for x in range(1,a+1):
        print("*"+(b-2)*" "+"*")
    print ("*"*b)
else:
    for x in range(1,a+1):
        print("*")