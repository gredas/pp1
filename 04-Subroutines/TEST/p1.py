def f(card_number):
    index1 = 0
    x = ""
    for number in card_number:
        if index1 < 2:
            x = str(x)+str(number)
        elif index1 < 12:
            x = str(x)+'*'
        else:
            x = str(x)+str(number)
        index1 = index1 + 1
    return x
print(f('5290312400019022'))
