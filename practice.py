from secrets import choice
import pandas as pd
from pandas import options

"""
age = 19
name = "Atharv"
status = "student"
print("{} is a {} years old {}".format(name, age, status))

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

msg = "Do you want to do more operations on the same numbers? (yes/no):"
bool = input(msg)
message = "What operation do you want to perform?"
options = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division"]

print(message)
for option in options:
    print(option)


def calculator():
 while bool.lower() == "yes":

  choice = int(input("Enter your choice: "))

 if choice == 1:
    print("Addition: ", add(a, b))
 elif choice == 2:
    print("Subtraction: ", subtract(a, b))
 elif choice == 3:
    print("Multiplication: ", multiply(a, b))
 elif choice == 4:
    print("Division: ", divide(a, b))
 else:
    print("Invalid choice")

print(msg)
if bool.lower() == "yes":
    calculator()
else:    print("Thank you for using the calculator!")


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Get initial numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def calculator(num1, num2):
    user_continue = "yes"
    
    while user_continue.lower() == "yes":
        print("\nWhat operation do you want to perform?")
        options = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division"]
        for option in options:
            print(option)

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print("Result: ", add(num1, num2))
        elif choice == 2:
            print("Result: ", subtract(num1, num2))
        elif choice == 3:
            print("Result: ", multiply(num1, num2))
        elif choice == 4:
            print("Result: ", divide(num1, num2))
        else:
            print("Invalid choice")

        # Ask to continue INSIDE the loop
        user_continue = input("\nDo you want to do another operation on these numbers? (yes/no): ")

# Start the program
calculator(a, b)
print("Thank you for using the calculator!")"""


# a = "aiscbgndssydbcyvcdv"

# ans = []
        
# for char in set(a):
#     if a.find(char) == a.rfind(char):
#         ans = min(ans, a.find(char))
                
#         print(ans) if ans != len(a) else print(-1)

# day = int(input("Enter the num: "))
# wd = ["Monday, Tuesday, wed, thu, fri, sat, sunday"]
# if day in range(0,8):
#     print(wd[day - 1])
# else :
#     print("invalid")

# match day:
#         case 1: print("Monday")
#         case 2: print("Tuesday")
#         case 3: print("Wednesday")
#         case 4: print("Thursday")
#         case 5: print("Friday")
#         case 6: print("Saturday")
#         case 7: print("Sunday")
#         case _: print("Invalid")

# low = int(input("enter the low num: "))
# high= int(input("enter the high num: "))

# count = high - low + 1
    
     # Apply the mathematical formula using integer division (//)
# total_sum = (count * (low + high)) // 2

# print(total_sum)



