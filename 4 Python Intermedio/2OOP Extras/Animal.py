class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        self.sounds="Makes a sound"
        return self.sounds
        
class Dog(Animal):
    def speak(self):
        self.sounds="Guau"
        return self.sounds

class Cat(Animal):
    def speak(self):        
        self.sounds= "Miau"
        return self.sounds

# Main

dog = Dog("Firulais")
print(dog.speak())  # Output: Guau

cat = Cat("Michi")
print(cat.speak())  # Output: Miau


