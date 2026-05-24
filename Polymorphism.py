# 1. Method Overriding (Run-time Polymorphism)

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()

# Output:
# Dog barks

# 2. Method Overloading (Same Method, Different Arguments)

class Math:
    def add(self, a, b=0, c=0):
        print(a + b + c)

obj = Math()

obj.add(5, 3)
obj.add(5, 3, 2)

# Output:
# 8
# 10

# 3. Operator Overloading

print(5 + 3)
print("Hello " + "World")

# Output:
# 8
# Hello World

# 4. Polymorphism with Different Classes

class Cat:
    def sound(self):
        print("Cat meows")

class Dog:
    def sound(self):
        print("Dog barks")

obj1 = Cat()
obj2 = Dog()

obj1.sound()
obj2.sound()

# Output:
# Cat meows
# Dog barks

