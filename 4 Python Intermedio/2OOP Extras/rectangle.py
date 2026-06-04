class Rectangle():
    def __init__(self,width,height):
        if width < 0 or height < 0:
            raise ValueError("Any of two numbers entered are negative, values must be positive...")
        self.width = width
        self.height = height

    def get_area(self):
        return self.height*self.width
    
    def get_perimeter(self):
        return (2*self.height)+(2*self.width)

#main
try:
    height = int(input("Enter Height value:"))
    width = int(input("Enter Width value:"))

    rectangle = Rectangle(width,height)
    
    print("The Area of the Rectangle is:",rectangle.get_area())
    print("The Perimeter of the Rectangle is:",rectangle.get_perimeter())
except ValueError as e:
    print(e)


