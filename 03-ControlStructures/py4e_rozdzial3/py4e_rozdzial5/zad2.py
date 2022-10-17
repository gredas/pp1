from re import X


x = 0
y = None
z = None
while x != "gotowe" :
    try:
        x = input('podaj liczbe\n')
        x = int(x)
        if z == None or x > int(z) :
            z = x
        if y == None or x < int(y) :
            y = x
        
    except ValueError:
        if x == "gotowe" :
            print(f"max {z} min {y}")
        else :
            print("zła wartość")
            continue