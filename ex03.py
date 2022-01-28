import math

class circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(slef):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
# 원의 둘레와 넓이
# 반지름  = 10

circle = circle(10)
print(" 원의 둘레와 넓이를 구합니다.")
print(" 원의 둘레:" , circle.get_circumference())
print(" 원의 넓이:" , circle.get_area())
print()