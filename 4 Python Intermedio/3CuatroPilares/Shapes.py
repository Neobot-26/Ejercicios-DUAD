from abc import ABC, abstractmethod

class ShapeFigures(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(ShapeFigures):
    def __init__(self,radius):
        self.radius = radius
    def calculate_perimeter(self):
        return 2*3.14*self.radius
    def calculate_area(self):
        return 3.14*self.radius**2

class Square(ShapeFigures):
    def __init__(self,side):
        self.side=side
    def calculate_perimeter(self):
        return self.side*4
    def calculate_area(self):
        return self.side**2

class Rectangle(ShapeFigures):
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def calculate_perimeter(self):
        return 2*self.height+2*self.width
    def calculate_area(self):
        return self.height*self.width

#Main
circle1 = Circle(5)
print(f"The perimeter:{circle1.calculate_perimeter()} m")
print(f"The Area:{circle1.calculate_area()} m2")
print("")
square1 = Square(4)
print(f"The perimeter:{square1.calculate_perimeter()} m")
print(f"The Area:{square1.calculate_area()} m2")
print("")
rectangle1 = Rectangle(3,6)
print(f"The perimeter:{rectangle1.calculate_perimeter()} m")
print(f"The Area:{rectangle1.calculate_area()} m2")
print("")
