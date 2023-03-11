def f(filename):
    t=0
    skrt=''
    flag=False
    for t in range(len(filename)):
        x=filename[t]
        if flag==True:
            skrt=skrt+filename[t]
        elif filename[t]=='.':
            skrt=skrt+'.'
            flag=True
        
        
        
    return skrt

    
