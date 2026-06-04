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
        for index_of_products in self.product_list:
            print(f"Name Article:{index_of_products.name}, Price:{index_of_products.price}, Quantity:{index_of_products.quantity}")

    def calculate_total_value_of_inventory(self):
        sumatory_inventory=0
        for index_of_products in self.product_list:
            sumatory_inventory+=index_of_products.price*index_of_products.quantity
        return sumatory_inventory
    
#Main
product1 = Product("Mouse",5000,3)
product2 = Product("Keyboard",8000,2)
inventory1 = Inventory()

#Add product
inventory1.add_product(product1)
inventory1.add_product(product2)

#Print List
inventory1.print_products()

#Calculate total value of inventary
print(f"The total value of inventary is:{inventory1.calculate_total_value_of_inventory()}")