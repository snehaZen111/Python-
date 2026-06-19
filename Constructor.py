# Constructor Example

class Student:

    def __init__(self):
        print("Constructor Called")

obj = Student()

# Output:
# Constructor Called



# Parameterized Constructor

class Student:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

obj = Student("Sneha")
obj.show()

# Output:
# Sneha

