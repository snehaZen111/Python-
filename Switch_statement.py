# 1. Switch Statement using Match Case (Python 3.10+)

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid Day")

# Output:
# Tuesday

# 2. Simple Calculator using Switch Statement

choice = "+"

a = 10
b = 5

match choice:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid Operator")

# Output:
# 15

# 3. Switch Statement using Dictionary Method

def monday():
    return "Monday"

def tuesday():
    return "Tuesday"

switch = {
    1: monday,
    2: tuesday
}

day = 1

print(switch.get(day, lambda: "Invalid Day")())

# Output:
# Monday

