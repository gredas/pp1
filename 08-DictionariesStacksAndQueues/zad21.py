import stack
flag = True
while flag:
    x = input()
    if x=='0' or x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or x=='8' or x=='9':
        x = int(x)
        stack.push(x)
    elif x=='+':
        y = stack.pop()+stack.pop()
        stack.push(y)
    elif x=='-':
        y = stack.pop()-stack.pop()
        stack.push(y)
    elif x=='*':
        y = stack.pop()*stack.pop()
        stack.push(y)
    elif x=='/':
        y = stack.pop()/stack.pop()
        stack.push(y)
    elif x == '=':
        stack.display()