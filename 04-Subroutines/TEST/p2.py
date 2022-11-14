def f(binary_number):
    for n in binary_number:
        if int(n) == 0 or int(n) == 1:
            flag = True
        else:
            flag = False
            return flag
            break
    return flag
print(f("0111011"))
            