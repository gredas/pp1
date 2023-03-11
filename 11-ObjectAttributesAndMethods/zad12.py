import math
class Area():
    @staticmethod
    def triangle(base, height):
        return base*height/2
    @staticmethod
    def rectangle(length,width):
        return length*width
    @staticmethod
    def circle(radius):
        return math.pi*radius**2
print(Area.circle(3))  # 28.274333882308138
print(Area.rectangle(4, 7))  # 28
print(Area.triangle(6, 2))  # 6

