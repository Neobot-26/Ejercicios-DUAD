class Person():
    def __init__(self,name):
        self.name = name

class Bus():
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passenger = []

    def add_passenger(self, person):
        if len(self.passenger)<self.max_passengers:
            self.passenger.append(person)
            print(f"{person.name} got inside the bus")
        else:
            print("The bus is full...")

    def substract_passenger(self):
        if self.passenger:
            person=self.passenger.pop()
            print(f"{person.name} has get out of the bus")
        else:
            print("There are not passengers in the bus")


# Main
bus1 = Bus(2)

passenger1=Person("Didier")
passenger2=Person("Alejandra")
passenger3=Person("Ana")

bus1.add_passenger(passenger1)
bus1.add_passenger(passenger2)
bus1.add_passenger(passenger3)

bus1.substract_passenger()
bus1.substract_passenger()
bus1.substract_passenger()