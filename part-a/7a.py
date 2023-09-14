import math
class Shape:
    def area(self):
        pass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
      return 0.5 * self.base * self.height

triangle = Triangle(5, 10)
print("Area of the Triangle:", triangle.area())