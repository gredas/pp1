number = range(1,31,1)
for x in number:
    if x%3 == 0 and x%5 == 0:
        print("BINGO")
    elif x%3 == 0:
        print("THREE")
    elif x%5 == 0:
        print("FIVE")
    else:
        print(x)
