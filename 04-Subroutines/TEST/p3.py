def f(amount_to_pay):
    x = amount_to_pay//5
    y = amount_to_pay%5
    z = y//2
    a = y%2
    sum = a + z + x
    return sum
print(f(10))