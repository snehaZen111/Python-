# 1. Simple if Statement

age = 18

if age >= 18:
    print("Eligible to vote")

# Output:
# Eligible to vote

# 2. if-else Statement

num = 10

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Output:
# Even Number

# 3. if-elif-else Statement

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Output:
# Grade B

# 4. Nested if Statement

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Under age")

# Output:
# Eligible to vote

# 5. Short Hand if Statement

num = 5

if num > 0: print("Positive Number")

# Output:
# Positive Number

# 6. Short Hand if-else (Ternary Operator)

num = 7

print("Even") if num % 2 == 0 else print("Odd")

# Output:
# Odd

# 7. Multiple Conditions using AND

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")

# Output:
# Entry Allowed

# 8. Multiple Conditions using OR

rain = False
holiday = True

if rain or holiday:
    print("Stay Home")

# Output:
# Stay Home

# 9. Condition using NOT

is_logged_in = False

if not is_logged_in:
    print("Please Login")

# Output:
# Please Login

# 10. Pass Statement in Condition

num = 10

if num > 0:
    pass

print("Program Running")

# Output:
# Program Running

