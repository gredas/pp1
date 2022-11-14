x = 0
y = 0
z = 0
while x != "gotowe" :
    try:
        x = input('podaj liczbe\n')
        y = y + int(x)
        z = z + 1
    except ValueError:
        if x == "gotowe" :
            print(f"suma to {y}, ile ich bylo to {z} a srednia {y/z}")
        else :
            print("zła wartość")
            continue