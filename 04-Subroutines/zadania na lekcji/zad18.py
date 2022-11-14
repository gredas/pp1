def sum_number_digits(x):
    y = 0
    for digit in x:
        y = y + int(digit)
    return y
print(sum_number_digits("7102"))