def f(dictionary,grade):
    flag=False
    x=dictionary["subject"]["grades"]
    for y in x:
        if y==grade:
            flag=True
    return flag
