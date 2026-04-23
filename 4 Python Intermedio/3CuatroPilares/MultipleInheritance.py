class GasolineVehicule:
    def refuel(self):
        print("Refueling Gasoline")

class ElectricVehicule:
    def charge(self):
        print("Charging Battery")

class HybridVehicule(GasolineVehicule,ElectricVehicule):
    def drive(self):
        print("Driving Hybrid Vehicule")

#Main
car = HybridVehicule()
car.drive()
car.refuel()
car.charge()
