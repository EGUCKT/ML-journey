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





"""Sum of first 50 positive integers ending with the given digit d"""
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

"""Number of digits in a number"""
# import math
# n = int(input("Enter a num and the script will tell the number of digits in it: "))
# if n == 0:
#     print("Bro zeroes can not be put in this!")
# else:
#     count = int(math.log10(n) + 1)
#     print(count)



"""Memory using dict, two sum"""
# num = [2, 4, 5, 8, 9, 7]
# target = 17
# result = []
# mem = {}
# complement = 0
# for i in range(len(num)):
#     crnum = num[i]
#     complement = target - crnum
#     if complement in mem:
#         result = [mem[complement], i]
#         break
#     mem[crnum] = i

# print(result)



"""Reversed num"""
# n = -1230

# maxl = 2 ** 31
# minl = -2 ** 31 - 1

# sign = 1
# if n < 0:
#     sign = -1
#     n = -n

# revnum = 0
# crnum = 0

# while n > 0:
#     crnum = n % 10
#     revnum = (revnum * 10) + crnum
#     n = n // 10
# result = sign * revnum
# print(result)


"""Palindrome check"""

# n = 13231
# revnum = 0
# og = n
# if n < 0:
#     print(False)
# else:
#     while n > 0:
#         crnum = n % 10
#         revnum = (revnum * 10) + crnum
#         n = n // 10
#     if og == revnum:
#         print(True)
#     else:
#         print(False)


"""Greatest common divisor of two nums"""
# a = 198
# b = 293

# while a > 0 and b > 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# if a == 0:
#     print(b)
# else:
#     print(a)



"""Find the median of two sorted arrays(naive approach O(n) complexity)"""
# num1 = [1, 3]
# num2 = [2, 4, 5]
# mrgd = sorted(num1 + num2)
# ln = len(mrgd)
# mid = len(mrgd) // 2

# if ln % 2 == 0:
#     print((mrgd[mid - 1] + mrgd[mid]) / 2)
# else:
#     print(mrgd[mid])



"""O(1) time complexity"""
# num1 = [1, 3]
# num2 = [2, 4]

# if len(num1) > len(num2):
#     num1, num2 = num2, num1

# m, n = len(num1), len(num2)
# totalhlf = (m + n + 1) / 2
# print(totalhlf)


"""Binary search approach (O(log(min(m, n))))"""

# num1 = [1, 3, 6, 7, 9]
# num2 = [2, 4, 5]

# if len(num1) > len(num2):
#     num1, num2 = num2, num1

# m, n = len(num1), len(num2)
# low, high = 0, m
# totalhlf = (m + n + 1) // 2

# while low <= high:
#     i = (low + high) // 2 # for this specific example i = 2
#     j = (totalhlf - i)

#     left1 = num1[i - 1] if i > 0 else float('-inf') #left1 = 3
#     right1 = num1[i] if i < m else float('inf') #right1 = 6

#     left2 = num2[j - 1] if j > 0 else float('-inf') #left2 = 4
#     right2 = num2[j] if j < n else float('inf') #right2 = 5

#     if left1 <= right2 and right1 >= left2:
#         if (m + n) % 2 == 0:
#             median = (max(left1, left2) + min(right1, right2)) / 2
#             print(median)        
#         else:
#             median = max(left1, left2)
#             print(median)
#         break
#     elif left1 > right2:
#         high = i - 1
#     else:
#         low = i + 1



"""Factorial finder"""
# fact = 1
# n = int(input("Enter a num to find it's factorial: "))
# for i in range(1, n+1):
#     fact *= i
# print(fact)


"""Meeting Rooms problem leetcode 252(Amazon)"""
# a = [[7, 9], [1, 3], [4, 6]]
# a.sort()
# final_result = True
# for i in range(len(a) - 1):
#     m = min(a[i+1])
#     m1 = max(a[i])
#     result = m1 < m
#     if result == False:
#         final_result = False
#         break

# print(final_result)




"""Check armstrong number"""
# n = 153
# count = len(str(n))
# sum = 0
# ans = n

# while n > 0:
#     ld = n % 10
#     sum += ld ** count
#     n = n // 10

# if sum == ans:
#     print(True)
# else:
#     print(False)




"""Find all divisors"""
# import math
# n = 6
# ans = []
# for i in range(1, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         ans.append(i)
#         if i != n // i:
#             ans.append(n // i)
# print(sorted(ans))


"""Find prime number"""

# import math
# n = 8
# ans = []
# for i in range(2, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         print(False)
#         break
# else:
#     print(True)


"""RECURSION"""

# name = 'Atharv'

# def printname(name, cnt=0, n=5):
#     if cnt == n:
#         return
#     else:
#         print(name, end=' ')

#     return printname(name, cnt + 1)

# printname(name, cnt=0, n=5)



"""Print num from 1 to n using recursion"""
# def printnum(num = 1, n = 10):
#     if n < num:
#         return
#     else:
#         print(num)

#     return printnum(num + 1, n)

# printnum(num = 1, n = 10)



"""Print num from n to 1"""

# n = 10
# def printnum(n):
#     if n == 0:
#         return
#     else:
#         print(n)

#     return printnum(n - 1)

# printnum(n)


"""sum of first n natural nums"""
# def printsum(n = 5):
#     if n == 0:
#         return 0
#     return n + printsum(n - 1)

# print(printsum(n=5))


"""Factorial of n"""

# def fact(n = 5):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)

# print(fact(n = 5))


"""Reverse a given array"""
# def revarr(arr, left, right):
#     if left >= right:
#         return
#     arr[left], arr[right] = arr[right], arr[left]
#     return revarr(arr, left + 1, right - 1)
# arr = [1, 2, 3, 4, 5]
# revarr(arr, 0, len(arr) - 1)

# print(arr)


"""Palindrome check"""

# def pal(left: int, right: int) -> bool:
#     if left >= len(st) // 2:
#         return True
#     if st[left] != st[right]:
#         return False
    
#     return pal(left + 1, right - 1)
# st = 'hannah'
# print(pal(0, len(st) - 1))

"""Palindrome check for leetcode"""
# import re
# def pal(left: int, right: int) -> bool:
#     if left >= len(gs) // 2:
#         return True
#     if gs[left] != gs[right]:
#         return False
#     return pal(left + 1, right - 1)

# s = ' '
# gs = re.sub(r'[^a-zA-Z]', "", s).lower()
# print(pal(0, len(gs) - 1))
# print(gs)


"""Remove duplicate elements from an array(Two pointer approach) leetcode(26)"""

# nums = [1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5]
# left = 0
# for i in range(1, len(nums)):
#     if nums[left] != nums[i]:
#         left += 1
#         nums[left] = nums[i]
        
# nums = nums[:left + 1]
# print(nums)


"""Remove duplicate elements from an array but keep at most 2 duplicate elements(leetcode 80)"""

# nums = [0,0,1,1,1,1,2,3,3]
# k = 2
# for i in range(2, len(nums)):
#     if nums[k - 2] != nums[i]:
#         nums[k] = nums[i]
#         k += 1
#     else:
#         pass
# nums = nums[:k]
# print(nums)


"""majority element from an array (leetcode 169)"""
"""Easy method using sorting when the majority element is present n/2 times in the array"""
# arr = [1, 2, 4, 1, 1, 1, 1, 4]
# j = len(arr)

# arr.sort()

# print(arr[j//2])

"""Using Boyer Moore's voting algorithm when the majority element is present n/2 times in the array"""

# nums = [1, 2, 4, 1, 1, 1, 1, 4]
# candidate = None
# count = 0

# for num in nums:
#     if count == 0:
#         candidate = num
#     if num == candidate:
#         count += 1
#     else:
#         count -= 1

# print(candidate)


"""For any array no matter the majority threshold"""
"""Using hashmap"""
# memory = {}
# arr = [1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5 ,6, 7, 8, 9, 2, 2, 2]
# max_count = 0
# max_element = None
# for i in arr:
#     if not i in memory:
#         memory[i] = 1
#     else:
#         memory[i] += 1
#     if memory[i] > max_count:
#         max_count = memory[i]
#         max_element = i
# print(max_element)


"""Fibonacci series using recursion and hashmap (leetcode 509)"""
# memo = {}
# def fib(n):
#     if n <= 1:
#         return n
#     if n in memo:
#         return memo[n]
#     if n not in memo:
#         memo[n] = fib(n - 1) + fib(n - 2)
#     return memo[n]

# print(fib(10))  # Example usage: prints the 10th Fibonacci number


"""Highest frequency counter using hashmap"""
# mem = {}
# nums = [1, 2, 2, 1, 3]
# count = 0
# for i in nums:
#     if i not in mem:
#         mem[i] = 1
#     else:
#         mem[i] += 1
# result = []
# for i, cnt in mem.items():
#     result.append([i, cnt])
# print(result)


"""Highest occuring element in an array using hashmap and if there are multiple elements with the same frequency then return the smaller one"""
# mem = {}
# nums = [1, 2, 2, 2, 3, 4, 4, 4, 5]
# for i in nums:
#     if i in mem:
#         mem[i] += 1
#     else:
#         mem[i] = 1
# result = []

# for i, cnt in mem.items():
#     result.append([i, cnt])

# print(max(result))


"""Max brackets needed to maintain equilibrium"""
# s = "())))"
# par = 0
# pir = 0

# if s == '':
#     print(0)
# else:
#     for i in s:
#         if i == '(':
#             par += 1
#         if i == ')':
#             pir += 1

# result = 0
# if par > pir:
#     result = par - pir
# elif par < pir:
#     result = pir - par
# elif par == pir:
#     print(0)
# print(result)


"""Sliding Window (Leetcode 1838)"""
# nums = [1, 4, 6, 10]
# k = 5
# nums.sort()
# left = 0
# curr = 0


# for right in range(len(nums)):
#     target = nums[right]
#     curr += target
#     if (right - left + 1) * target - curr > k:
#         curr -= nums[left]
#         left += 1
        
        
# print(len(nums) - left)



"""Selection sort"""

# nums = [3, 2, 3, 4, 5]
# left = 0

# for i in range(len(nums)):
#     left = i
#     for j in range(i + 1, len(nums)):
#         if nums[j] < nums[left]:
#             left = j
#     nums[i], nums[left] = nums[left], nums[i]

# print(nums)


"""Exchange sort"""
# nums = [5, 4, 4, 1, 1]
# left = 0


# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[j] < nums[left]:
#             nums[j], nums[left] = nums[left], nums[j]
#     left += 1

# print(nums)


"""Bubble sort (Brute Force)"""
# nums = [5, 4, 4, 1, 1]
# left = 0


# for i in range(len(nums)):
#     for j in range(len(nums) - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]

# print(nums)


"""Bubble sort (Optimized approach(-i))"""
# nums = [5, 4, 4, 1, 1]
# left = 0


# for i in range(len(nums)):
#     for j in range(len(nums) - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]

# print(nums)


"""Insertion Sort"""

# nums = [5, 4, 4, 1, 1]

# for i in range(1, len(nums)):
#     key = nums[i]
#     j = i - 1
    
#     while j >= 0 and nums[j] > key:
#         nums[j + 1] = nums[j]
#         j -= 1
        
#     nums[j + 1] = key

# print(nums)


"""Merge Sort (Optimized (without extra memory))"""
# def divide(arr: list[int]) -> list[int]:
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     divide(left)
#     divide(right)

#     i = 0
#     j = 0
#     k = 0
#     nums = []

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1
#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1
#     return arr

# print(divide(arr = [2, 4, 2, 1, 6, 5, 3, 9, 8, 1]))


"""Recursive Bubble Sort"""

# def bbl(nums: list[int], n = None) -> list[int]:
#     if n is None:
#         n = len(nums)
#     if n == 1:
#         return nums
#     for i in range(n - 1):
#         if nums[i] > nums[i + 1]:
#             nums[i + 1], nums[i] = nums[i], nums[i + 1]
#     return bbl(nums, n - 1)
# print(bbl(nums = [4, 3, 2, 16, 4, 2, 1]))


"""Recursive Insertion Sort"""

# def ins(nums: list[int], n = None):
#     if n is None:
#         n = len(nums)
#     if n <= 1:
#         return
#     ins(nums, n - 1)
#     key = nums[n - 1]
#     j = n - 2
#     while j >= 0 and nums[j] > key:
#         nums[j + 1] = nums[j]
#         j -= 1
#     nums[j + 1] = key
#     return nums

# print(ins(nums = [1, 2, 1, 6, 3]))


"""Quick Sort"""

# def partition(nums: list[int], low: int, high: int) -> int:
#     # Choose the first element as the pivot
#     pivot = nums[low]
#     i = low
#     j = high

#     while i < j:
#         # Move 'i' right as long as elements are smaller than or equal to pivot
#         while i <= high and nums[i] <= pivot:
#             i += 1
        
#         # Move 'j' left as long as elements are strictly greater than pivot
#         while j >= low and nums[j] > pivot:
#             j -= 1
        
#         # If pointers haven't crossed yet, swap the misplaced elements
#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]
            
#     # Once i and j cross, 'j' is the correct final home for the pivot.
#     # Swap the pivot into its final resting place.
#     nums[low], nums[j] = nums[j], nums[low]
    
#     return j  # Return the index where the pivot settled


# def quickSortHelper(nums: list[int], low: int, high: int):
#     # BASE CASE: If the section has 0 or 1 elements, it's already sorted
#     if low < high:
#         # Step 1: Put the pivot in its right spot and get its index
#         pivot_index = partition(nums, low, high)
        
#         # Step 2: Recursively sort the left side of the pivot
#         quickSortHelper(nums, low, pivot_index - 1)
        
#         # Step 3: Recursively sort the right side of the pivot
#         quickSortHelper(nums, pivot_index + 1, high)


# def quickSort(nums: list[int]) -> list[int]:
#     quickSortHelper(nums, 0, len(nums) - 1)
#     return nums


# my_list = [25, 57, 48, 37, 12, 92, 86, 33]
# print(quickSort(my_list))


"""Largest number in an array"""

# nums = [2, 3, 1, 8, 5, 1]

# max = 0
# for i in nums:
#     if i > max:
#         max = i
# print(max)

"""Second largest element in an array"""

# nums = [8, 8, 7, 6, 5]

# maxi = float("-inf")
# lmax = float("-inf")

# for i in nums:
#     if i > maxi:
#         lmax = maxi
#         maxi = i
#     elif i > lmax and i != maxi:
#         lmax = i
# if lmax == float("-inf"):
#     lmax = -1

# print(lmax)


"""Check if the array is sorted or rotated (leetcode 1752)"""

# nums = [6, 1, 3, 4]
# print(sum(nums[i] > nums[(i + 1) % len(nums)] for i in range(len(nums))) <= 1)


"""Move zeroes to the end of the array (in place) (Leetcode 283)"""
"""BRUTE FORCE APPROACH (TLE error)"""
# nums = [0, 1, 0, 3, 12, 0, 2]
# for i in range(len(nums) - 1):
#     for j in range(len(nums) - 1):
#         if nums[j] == 0:
#             nums[j] , nums[j + 1] = nums[j + 1], nums[j]

# print(nums)

"""Optimal two pointer approach"""
# nums = [0, 1, 0, 3, 12, 0, 2]
# left = 0
# for i in range(len(nums)):
#     if nums[i] != 0:
#         nums[i], nums[left] = nums[left], nums[i]
#         left += 1
# print(nums)


