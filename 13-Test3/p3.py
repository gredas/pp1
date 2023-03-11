import builtins
n = int(input())
integer_list = input().split()
for x in integer_list:
    x = int(x)
    t = hash(x)
    print(t,end="")