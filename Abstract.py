# Abstract Class in Python (OOP Concept)

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass   # No implementation here

# Child Class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child Class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating objects
obj1 = Dog()
obj2 = Cat()

obj1.sound()
obj2.sound()

# Output:
# Dog barks
# Cat meows


---

# Abstract Class with Constructor

from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self):
        print(self.name, "Area = πr^2")

obj = Circle("Circle")
obj.area()

# Output:
# Circle Area = πr^2

