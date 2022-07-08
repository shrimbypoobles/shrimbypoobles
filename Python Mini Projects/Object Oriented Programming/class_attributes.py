# Class Attributes & Class Methods
class Person:
    number_of_people = 0 # Class Attribute (does not use self(defined for entire class))
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
     
    @classmethod  # denotes class method 
    def number_of_people_(cls): # Class Method, acts on the class itself, does not have access to any instance
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
p1 = Person("Justin")
p2 = Person("Caroline")
print(Person.number_of_people_())