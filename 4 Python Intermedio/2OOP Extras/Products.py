class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.product_list = []

    def add_product(self,product):
        self.product_list.append(product)

    def print_products(self):
        for index in self.product_list:
            print(f"Name:{index.name}, Price:{index.price}, Quantity:{index.quantity}")

    def calculate_total_value_of_inventory(self):
        sum=0
        for index in self.product_list:
            sum=sum+index.price*index.quantity
        return sum
    
#Main
product1 = Product("Mouse",5000,3)
product2 = Product("Keyboard",8000,2)
Inventory1 = Inventory()

#Add product
Inventory1.add_product(product1)
Inventory1.add_product(product2)

#Print List
Inventory1.print_products()

#Calculate total value of inventary
print(f"The total value of inventary is:{Inventory1.calculate_total_value_of_inventory()}")