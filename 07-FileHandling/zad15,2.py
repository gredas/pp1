with open(".\\countries.txt", "r") as file:
    for i, line in enumerate(file, 1):
        if i % 5 != 0:
            print(i, line)
        else:
            print(i,line)
            input("kliknij enter: ")
        