class Employee:
    def __init__(self,name,salary):
        self._name = name
        self._salary = 0
        self._salary = salary

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name=value

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("The salary can not be negative")
        self._salary = value

    def promote(self,percent_increase):
        self._salary += percent_increase*self._salary
    
#main
employee=Employee("Ana",1000)
employee.promote(0.1)
print(employee.salary)
