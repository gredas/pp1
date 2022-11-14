x = int(input('enter x\n'))
y = int(input('enter y\n'))
if x == 0 and y == 0:
    print("center")
elif x >= 0 and y>=0:
    print(f'P({x},{y}) first quadrant')
elif x >= 0 and y <= 0:
    print(f"P({x},{y}) second quadrant")
elif x <= 0 and y <= 0:\
    print(f'P({x},{y}) third quadrant')
elif x<=0 and y>=0:
    print(f'P({x},{y}) fourth quaadrant')