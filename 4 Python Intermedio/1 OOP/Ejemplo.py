class Car:
        wheel_number=4

        def my_first_method(self):
                print("Hello OOP World!")
        def show_history(self, miles, crashes):
                print(f"This car has {miles} miles and {crashes} crashes and {self.wheel_number} wheels")

my_car=Car()
my_car.my_first_method()
my_car.show_history(45000,2)
