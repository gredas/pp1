import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
average = 0
sum = 0
t = 0
for x in temperatures:
    x = int(x)
    sum = sum + x
    t+=1
print(sum/t)