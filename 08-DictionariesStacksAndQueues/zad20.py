import stack
n = 82824654564
while n!=0:
    if n%2==0:
        stack.push(0)
    else:
        stack.push(1)
    n = n//2
    flag = not stack.empty()
while flag:
    print(stack.pop(),end='')
    flag = not stack.empty()

