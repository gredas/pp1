def count(a,b):
    count = 0
    for letter in b:
        if letter == a:
            count = count + 1
    print(count)
count("a","banan")