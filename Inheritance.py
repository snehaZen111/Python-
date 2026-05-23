# 1. Single Inheritance

class Parent:
    def show(self):
        print("This is Parent Class")

class Child(Parent):
    def display(self):
        print("This is Child Class")

obj = Child()
obj.show()
obj.display()

# Output:
# This is Parent Class
# This is Child Class

# 2. Multiple Inheritance

class Father:
    def skills1(self):
        print("Father: Driving")

class Mother:
    def skills2(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

obj = Child()
obj.skills1()
obj.skills2()

# Output:
# Father: Driving
# Mother: Cooking

# 3. Multilevel Inheritance

class Grandparent:
    def grand(self):
        print("Grandparent Class")

class Parent(Grandparent):
    def parent(self):
        print("Parent Class")

class Child(Parent):
    def child(self):
        print("Child Class")

obj = Child()
obj.grand()
obj.parent()
obj.child()

# Output:
# Grandparent Class
# Parent Class
# Child Class

# 4. Hierarchical Inheritance

class Parent:
    def show(self):
        print("Parent Class")

class Child1(Parent):
    def display1(self):
        print("Child1 Class")

class Child2(Parent):
    def display2(self):
        print("Child2 Class")

obj1 = Child1()
obj1.show()
obj1.display1()

obj2 = Child2()
obj2.show()
obj2.display2()

# Output:
# Parent Class
# Child1 Class
# Parent Class
# Child2 Class

# 5. Hybrid Inheritance

class A:
    def methodA(self):
        print("Class A")

class B(A):
    def methodB(self):
        print("Class B")

class C(A):
    def methodC(self):
        print("Class C")

class D(B, C):
    def methodD(self):
        print("Class D")

obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()

# Output:
# Class A
# Class B
# Class C
# Class D

