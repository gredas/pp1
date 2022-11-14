def phone_keypad():
    a = range(1,4,1)
    b = range(0,7,3)
    c = None
    for x in b :
        print()
        for y in a:
            c = x + y
            print(c, end=" ")
phone_keypad()