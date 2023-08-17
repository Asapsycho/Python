#polymorphism allows different objects to repond to
#the same method in there own way
class Shape:
    def area(self):
        pass
class Circle(Shape):
        def __init__(self,radius):
            self.radius=radius
        def area(self):
            return 3.14 *self.radius **2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side **2
    #creating objects
shape= [Circle(5),Square(6)]

for i in shape:
    print("Area :",i.area())