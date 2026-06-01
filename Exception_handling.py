# 1. Basic Try Except

try:
    print(10 / 0)
except:
    print("Error Occurred")

# Output:
# Error Occurred

# 2. Try Except with Exception Type

try:
    num = int("abc")
except ValueError:
    print("Invalid Input")

# Output:
# Invalid Input

# 3. Try Except Else

try:
    num = 10 / 2
except:
    print("Error Occurred")
else:
    print("Division Successful")

# Output:
# Division Successful

# 4. Try Except Finally

try:
    print(10 / 2)
except:
    print("Error Occurred")
finally:
    print("Program Ended")

# Output:
# 5.0
# Program Ended

# 5. Multiple Except Blocks

try:
    num = int("abc")
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Division by Zero")

# Output:
# Value Error

# 6. ZeroDivisionError Handling

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot Divide by Zero")

# Output:
# Cannot Divide by Zero

# 7. IndexError Handling

try:
    my_list = [10, 20, 30]
    print(my_list[5])
except IndexError:
    print("Index Out of Range")

# Output:
# Index Out of Range

# 8. FileNotFoundError Handling

try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File Not Found")

# Output:
# File Not Found

# 9. User Defined Exception

age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)

# Output:
# Age cannot be negative

# 10. Exception Object

try:
    print(10 / 0)
except Exception as e:
    print("Error:", e)

# Output:
# Error: division by zero

