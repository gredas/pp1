def how_many(x,y):
    index = 0
    for letter in y:
        if letter == x:
            index = index + 1
    return index

print(how_many('e','You never get a second chance to make a first impression'))
