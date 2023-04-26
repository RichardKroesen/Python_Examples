class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # square is denoted with ** in python 
        return 3.14 * self.radius ** 2

shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(shape.area())
