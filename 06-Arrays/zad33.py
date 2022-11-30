arr = [2,22,222,222,22,2]
print('-'*5*len(arr))
for x in arr:
    print('|',end="")
    if x<=9 and x>=0:
        print(f'  {x}',end="")
    elif x<=99 and x>=10:
        print(f' {x}',end="")
    elif x<=999 and x>=100:
        print(f'{x}',end="")
    print('|',end="")
print()
print('-'*5*len(arr))