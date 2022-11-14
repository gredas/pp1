def sum(n):
    x = 0
    y = 0
    if n == 1:
        return 1
    while x != n:
        x = x + 1
        y = y + x
    return y
print(sum(10))




