with open('numbers.txt','r') as x:
    with open('copylines.txt','w') as y:
        for z in x:
            y.write(f'{z}\n')