def f(array2D):
    row=0
    rowmin=0
    summin=0
    sum=0
    t=0
    for x in array2D:
        for y in x:
            if t==0:
                summin+=y
    t=1
    for x in array2D:
        for y in x:
            sum+=y
        if sum<=summin:
            summin=sum
            rowmin=row
        row+=1
        sum=0
    return rowmin




