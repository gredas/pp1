def same(n,m):
    y=0
    if len(n)==len(m):
        for x in n:
            if x==n[y]:
                flag=True
            else:
                flag=False
                break
    else:
        print(f'array1:',end=' ')
        for sk in n:
            print(sk,end=' ')
        print()
        print(f'array1:',end=' ')
        for sk in m:
            print(sk,end=' ')
        print()
        print('Comparison:not same')
    if flag==True:
                print(f'array1:',end=' ')
                for sk in n:
                    print(sk,end=' ')
                print(f'array1:',end=' ')
                for sk in m:
                    print(sk,end=' ')
                print('Comparison:same')
                y+=1
    else:
                print(f'array1:',end=' ')
                for sk in n:
                    print(sk,end=' ')
                print(f'array1:',end=' ')
                for sk in m:
                    print(sk,end=' ')
                print('Comparison:not same')
same(["water","book","sky"],["water","book","sky"])