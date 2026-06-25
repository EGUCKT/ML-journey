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



"""First unique character"""
# a = "aiscbgndssydbcyvcdv"

# ans = float('inf')
        
# for char in set(a):
#     if a.find(char) == a.rfind(char):
#         ans = min(ans, a.find(char))
           
# if ans != len(a):
#     print(ans)
# else :
#     print(-1)



"""Without switch case for weekdays by nums"""
# day = int(input("Enter the num: "))
# wd = ["Monday", "Tuesday", "wed", "thu", "fri", "sat", "sunday"]

# if day in range(1, 8):
#     print(wd[day - 1])
# else:
#     print("invalid")




"""Switch case for days"""
# match day:
#         case 1: print("Monday")
#         case 2: print("Tuesday")
#         case 3: print("Wednesday")
#         case 4: print("Thursday")
#         case 5: print("Friday")
#         case 6: print("Saturday")
#         case 7: print("Sunday")
#         case _: print("Invalid")




"""Sum of integers from low to high"""
# low = int(input("enter the low num: "))
# high= int(input("enter the high num: "))

# count = high - low + 1
    
#      #Apply the mathematical formula using integer division (//)
# total_sum = (count * (low + high)) // 2

# print(total_sum)





"""Sum of first 50 positive integers ending wiht the given digit d"""
# d = int(input("Enter the num; "))

# count = 0
# crnum = d
# total = 0

# while count < 50 :
#     total += crnum
#     crnum += 10
#     count += 1

# print(total)





"""Reverse the given array"""
# arr = [1,2,3,3,5,4]
# n = 6
# m = 0
# while m < n:
#     n -= 1
#     arr[m], arr[n] = arr[n], arr[m]
#     m += 1
# print(arr)





"""Square of stars"""
# for i in range(5):
#     for j in range(5):
#         print('*', end=" ")
#     print()




"""Right angled triangle of stars"""
# n = 5
# for i in range(n):
#     print('*' * (i + 1))





"""Right angled triangle of digits"""
# for i in range(6):
#     for j in range(1, i + 1):
#         print(j, end=" ")    
#     print()



"""Right angled triangle of digits w.r.t. their row number, ex: 1, 22, 333, etc"""
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=" ")
#     print()





"""Reversed right angled triangle of stars"""
# for i in range(5):
#     for j in range(5 - i):
#         print('*', end=" ")
#     print()






"""Reversed right angled triangle of digits"""
# for i in range(5):
#     for j in range(1, 5 - i + 1):
#         print(j, end="")
#     print()





"""Subarray of the maximum total"""
# s = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# running_total = s[0]
# total = s[0]

# for i in range(1, len(s)):
#     running_total = max(s[i], running_total + s[i])
#     total = max(total, running_total)
# print(total)



"""Sum of all positive integers from the low num to high num"""
# sum = 0
# low = 3
# high = 8
# for i in range(low, high + 1):
#     sum = i + sum
# print(sum)



"""Right angled pyramid"""
# n = 5
# for i in range(n):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()



"""Right angled reverse pyramid"""
# n = 5
# for i in range(n):
#     for j in range(i, n, +1):
#         print("*", end=" ")
#     print()




"""Right angled reverse triangle of digits"""
# n = 5
# for i in range(1, n+1):
#     for j in range(1, (n+1) - i + 1):
#         print(j, end=" ")
#     print()




"""Left angled triangle"""
# n = 10
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()


"""Pyramid of stars"""
# n = 10
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for k in range(2*i+1):
#         print("*", end=" ")
#     print()


"""Left angled reverse triangle"""
# n = 10
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for k in range(n - i - 1):
#         print("*", end=" ")
#     print()



"""Reversed Pyramid of stars"""
# n = 10

# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end="")
#     for k in range(2 * n - (2 * i + 1)):
#         print("*", end="")
#     print()





"""Diamond of stars"""
# n = 10
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for k in range(2*i+1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(2 * n - (2 * i + 1)):
#         print("*", end=" ")
#     print()



"""Right angled diamond"""
# n = 10

# for i in range(n):
#     for j in range(i + 1):
#         print("*", end="")
#     print()
# for i in range(n):
#     for j in range(n - i - 1):
#         print("*", end="")
#     print()



"""Binary right angled triangle"""
"""Bad Practice"""
# nums = [1, 0]
# n = 10

# for i in range(n):
#     for j in range(i + 1):
#         for u in nums:
#             print(nums[u], end="")
#     print()



"""Best Practice"""
# n = 10

# for i in range(n):
#     if i % 2 == 0:
#         start = 1
#     else:
#         start = 0
#     for j in range(i + 1):
#         print(start, end="")
#         start = 1 - start
#     print()




"""Two right angled pyramids of digits(reversed) together with space in between increasing"""
# n = 10

# for i in range(1, n):
#     for j in range(1, i+1):
#         print(j, end="")
#     for k in range(2 * n - (2 * i + 2)):
#         print(" ", end="")
#     for u in range(i, 0, -1):
#         print(u, end="")
#     print()



"""Print nums for increasing order per row for the number of n rows"""
# n = 10
# num = 1
# for i in range(1, n):
#     for j in range(1, i + 1):
#         print(num, end="")
#         num +=1
#     print()



"""Print ABCD for increasing order starting from A for each row"""
# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(65 + j), end="")
#     print()


"""Print ABCD for increasing order on each row with number of repeated A, BB, CCC and so on..."""
# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(65 + i), end="")
#     print()




"""Print ABCD for decreasing order starting from A for each row n"""
# n = 10
# for i in range(n):
#     for j in range(0, n - (i + 1) + 1):
#         print(chr(65 + j), end="")
#     print()



"""Print ABCD pyramid with shared characters invertedly"""
# n = 10
# for i in range(n):
#     for k in range(n - i - 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print(chr(65 + j), end="")
#     for l in range(i, 0, -1):
#         print(chr(65 + l - 1), end="")
#     print()




"""print ABCD from the last character outside and the first character in the core of the right angled triangle"""
# n = 5
# for i in range(1, n + 1):
#     for j in range(i, 0, -1):
#         print(chr(65 + n - j), end="")
#     print()




"""Print two triangles pointing the sharp side towards the other"""
# n = 5
# for i in range(n + 1):
#     for j in range(i + 1):
#         print("*", end="")
#     for k in range(0, 2 * n - (2 * i)):
#         print(" ", end="")
#     for l in range(i + 1):
#         print("*", end="")
#     print()

# for i in range(n):
#     for j in range(n - i):
#         print("*", end="")
#     for k in range(0, 2 * (i + 1)):
#         print(" ", end="")
#     for l in range(i + 1, n + 1):
#         print("*", end="")
#     print()




"""Print empty diamond shape of stars"""
# n = 5
# for i in range(n):
#     for j in range(n - i):
#         print("*", end="")
#     for k in range(0, 2 * (i + 1)):
#         print(" ", end="")
#     for l in range(i + 1, n + 1):
#         print("*", end="")
#     print()

# for i in range(n + 1):
#     for j in range(i + 1):
#         print("*", end="")
#     for k in range(0, 2 * n - (2 * i)):
#         print(" ", end="")
#     for l in range(i + 1):
#         print("*", end="")
#     print()


"""Empty rectangle of stars"""
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


"""Print a square of n numbers where the min of n is in the core"""
# n = 5
# for i in range(2 * n - 1):
#     for j in range(2 * n - 1):
#         top = i
#         left = j
#         bottom = (2 * n - 2) - i
#         right = (2 * n - 2) - j
#         minDist = min(top, left, right, bottom)
#         print(n - minDist, end=" ")
#     print()


# import math
# n = int(input("Enter a num and the script will tell the number of digits in it: "))
# if n == 0:
#     print("Bro zeroes can not be put in this!")
# else:
#     count = int(math.log10(n) + 1)
#     print(count)

"""WORKING ON REAL WORLD DATA FROM MY COLLEGE"""
import matplotlib as mpl
import numpy as np

df = pd.read_csv("atsres.csv")

sf = df

"""dealing with str, and symbols like '/', '-', '%' and convertign them to NaN and then filling with median while converting to float"""
sf['ATS Resume Score'] = sf['ATS Resume Score'].replace(r"[^\d.-]", np.nan, regex=True) 

sf['ATS Resume Score'] = pd.to_numeric(sf['ATS Resume Score'], errors= "coerce")

sf['ATS Resume Score'] = sf['ATS Resume Score'].fillna(sf['ATS Resume Score'].median())

print('The mean is:')
print(sf['ATS Resume Score'].mean())

print('The lowest score is:')
print(sf['ATS Resume Score'].min())
print("Whose index is:", sf['ATS Resume Score'].idxmin())
print(sf.loc[202])

print('The highest score is:')
print(sf['ATS Resume Score'].max())
print("Whose index is:", sf['ATS Resume Score'].idxmax())
print(sf.loc[72])
