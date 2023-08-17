#inheritance allows one class to inherit attributes
#and methods from other class
class Animal:
    def __init__(self,name):
        self.name=name
class Building:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
        def speak(self):
            return "woof"
class Cat(Animal):
            def speak(self):
                return  "Meows"

class Karamathproperties(Building):
                def speak(self):
                    return "ksh.205.000"
            #this are objects
doggi=Dog("Ghost")
paka=Cat("Omar")
office=Karamathproperties("7Vizi")
print(doggi.speak())
print(paka.speak())
print(office.speak())