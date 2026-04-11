class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)


# Main
circle1 = Circle(5)
print("Area of the circle:", circle1.get_area())