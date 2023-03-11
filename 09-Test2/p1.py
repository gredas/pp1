def f(player1,player2):
    t = 0
    sum1=0
    sum2=0
    while t!=len(player1):
        if player1[t]=='A' or player1[t]=='Q' or player1[t]=='K' or player1[t]=='J' or player1[t]=='10':
            sum1+=10
        elif player1[t]=="9":
            sum1+=9
        elif player1[t]=="8":
            sum1+=8
        elif player1[t]=="7":
            sum1+=7
        elif player1[t]=="6":
            sum1+=6
        elif player1[t]=="5":
            sum1+=5
        elif player1[t]=="4":
            sum1+=4
        elif player1[t]=="3":
            sum1+=3
        elif player1[t]=="2":
            sum1+=2
        elif player1[t]=="1":
            sum1+=1
        t+=1
    t=0
    while t!=len(player2):
        if player2[t]=='A' or player2[t]=='Q' or player2[t]=='K' or player2[t]=='J' or player2[t]=='10':
            sum2+=10
        elif player2[t]=="9":
            sum2+=9
        elif player2[t]=="8":
            sum2+=8
        elif player2[t]=="7":
            sum2+=7
        elif player2[t]=="6":
            sum2+=6
        elif player2[t]=="5":
            sum2+=5
        elif player2[t]=="4":
            sum2+=4
        elif player2[t]=="3":
            sum2+=3
        elif player2[t]=="2":
            sum2+=2
        elif player2[t]=="1":
            sum2+=1
        t+=1
    if sum1>=sum2:
        return True
    else:
        return False

print(f('AA87','AA88'))



