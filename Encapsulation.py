# 1. Basic Encapsulation

class Student:
    def __init__(self):
        self.__name = "Sneha"   # Private Variable

    def show(self):
        print(self.__name)

obj = Student()
obj.show()

# Output:
# Sneha


---

# 2. Encapsulation using Getter Method

class Student:
    def __init__(self):
        self.__name = "Sneha"

    def get_name(self):
        return self.__name

obj = Student()

print(obj.get_name())

# Output:
# Sneha


---

# 3. Encapsulation using Setter Method

class Student:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

obj = Student()

obj.set_name("Sneha")
print(obj.get_name())

# Output:
# Sneha


---

# 4. Encapsulation with Private Data

class Bank:
    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print(self.__balance)

obj = Bank()

obj.show_balance()

# Output:
# 5000


---

# 5. Accessing Private Variable Directly

class Student:
    def __init__(self):
        self.__name = "Sneha"

obj = Student()

try:
    print(obj.__name)
except:
    print("Cannot Access Private Variable")

# Output:
# Cannot Access Private Variable

