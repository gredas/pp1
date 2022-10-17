def count(a, b):
    ile = 0
    for letter in a:
        if letter == b:
            ile += 1
    print(ile)

count("eeef", "e")