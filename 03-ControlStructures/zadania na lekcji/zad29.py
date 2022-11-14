a = None
sum = 0
quantity = 0
mean = 0
b = int(input('enter number: '))
while b != 0:
    sum = sum + b
    quantity += 1
    mean = sum/quantity
    b = int(input('enter number: '))
print(f'q:{quantity}, s:{sum}, m:{mean}')



