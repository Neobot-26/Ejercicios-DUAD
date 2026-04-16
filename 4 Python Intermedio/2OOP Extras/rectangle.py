class Rectangle():
    def __init__(self):
        self.width = int(input("Enter height of the rectangle:"))
        self.height = int(input("Enter width of the rectangle:"))
    def get_area(self):
        if self.width<0 or self.height<0:
            print("Any of two numbers entered are negative, values must be positive")
        else:
            return self.height*self.width
    def get_perimeter(self):
        if self.width>0 and self.height>0:
            return (2*self.height)+(2*self.width)

#main
rectangle1 = Rectangle()
print("The Area of the Rectangle is:", rectangle1.get_area())
print("The Perimeter of the Rectangle is:", rectangle1.get_perimeter())

