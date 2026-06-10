# Interface Example in Python

from abc import ABC, abstractmethod

# Interface
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Implementing Interface
class Dog(Animal):

    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()

# Output:
# Dog barks
