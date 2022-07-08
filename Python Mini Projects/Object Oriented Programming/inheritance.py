from unicodedata import name

class Pet: # Parent Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
        
    def speak(self):
        if Dog:
            print("Bark")
        else:
            print("Meow")

class Cat(Pet): # Child Class
    def __init__(self, name, age, color):
        super().__init__(name, age) # Super calls upper lvl parent class initialization
        self.color = color
        
    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, I'm {self.color} colored.")
        
class Dog(Pet): # Child Class 
    def speak(self):
        print("Bark")


c = Cat("Josie", 1, "Tortie")
c.show()
c.speak()
p = Pet("Bobie", 2)
p.show()
p.speak()
d = Dog("Philly", 7)
d.show()
d.speak()
d = Dog("Ollie", 10)
d.show()
d.speak()