def occurs(array):
    number=input('Podaj liczbe: \n')
    
    for x in array:
        if x==int(number):
            flag=True
            break
        else:
            flag=False
    if flag==True:
        print(f'Number {number} appears in the array {array}')
    else:
        print(f'{number} not appears')
        x=input()
occurs([15,38,7,23,14])