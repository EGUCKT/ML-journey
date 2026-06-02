from altair import value
import pandas as pd
"""
#variable
message = "hiiiii everynione!"
print(message)

#normal output
print("Hello, World!")

#finding length of string
print(len(message))

#slicing string
print(message[7:])

#changing case
print(message.upper())
print(message.lower())

#replacing substring
print(message.replace("i", "a"))

#finding substring
print(message.find("every"))

#counting occurrences of a substring
print(message.count("i"))

#replacing substring
message = message.replace("everynione", "everyone")
print(message)

#combnining strings
greeting = "Hello"
name = "Atharv"
message = greeting.upper() + ' ,' + name + "!"
print(message)

#using placeholder
age = 19
name = "Atharv"
message = "{}, you are {} years old!".format(name, age)
print(message)

#finding type of variable
print(type(age))

#Arithmetic opertions
a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
#Incrementing and decrementing
a += 1
print(a)
b -= 1
print(b)

#casting and converting str to int
num_str = "100"
num_int = int(num_str)
print(num_int + 50)

#lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.insert(1, "blueberry")
print(fruits)
fruits.append("date")
print(fruits)
tasty_fruits = ["mango", "pineapple"]
fruits.extend(tasty_fruits)
print(fruits)
fruits.remove("banana")
print(fruits)

nums = [5, 2, 9, 1, 5, 6]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

#dictionaries
haha = {'name': 'Atharv', 'age': 19, 'city': 'Pune'}
print(haha)
print(haha['name'])
print(haha.get('job', 'Nahi pta bhai'))
haha['job'] = 'unemployed'
print(haha.get('job'))

list = [1, 5, 6, 59, 23, 90, 12, 34, 78, 11, 3, None, 45, 67, 89, 100, 22, 44, 55, 88, 77, 33, 21, 9, 8, 7, 4, 2]
for num in list:
    if num is None:
        continue
    if num >= 90:
        break
    print(num)

try:
    a = open('testfile.txt')
except FileNotFoundError:
    print("Sorry this file is not found!")
else:
    print(a.read())
    a.close()
finally:
    print('executed in -0.15 seconds')

str_a = '5'
int_b = 100
str_a = int(str_a)
add = str_a + int_b
print(add)

try:
    lmno = [('atharv'), ('rahul'), ('rohan')]
    print(lmno[4])
except:
    if True:
        print("There is no index like that in the list")

try:
    str_a = '5'
    int_b = 100
    add = str_a + int_b
    print(add)
except:
    str_a = int(str_a)
    add = str_a + int_b
    print(add)
finally:
    print("Execution complete.")


try:
    print(lala)
except NameError:
    print("Variable 'lala' is not defined.")

from gettext import find
try:
    new_dict = {
    'name': 'Atharv',
    'age': 19,
    'city': 'Pune'
}
    for a in new_dict:
      print(find.new_dict[a])
except:
    print("An error occurred while accessing the dictionary.")
finally:
    print("Dictionary access attempt complete.")


try:
    data = [10, 20, None, 30]
    for value in data:
        if value == None:
            continue
        print(value)
except:
    print("An error occurred during data processing.")


#bad approach
def haha():
 try:    
    i = 1
    while i <= 10:
           if i == 5:
            i += 1
            continue
           print(i)
           i += 1
 except:
    print("An error occurred in the loop.")

haha()


#better approach
def haha_better():
   for i in range(1, 11):
      if i == 5:
         continue
      print(i)

haha_better()


def hello(greeting, name):
    return f"{greeting}, {name}!"
print(hello("Hello", input("Enter your name: ")))


try:
 def big(a, b):
    if b>a:
        return b
    else:
        return a

 def bigger(a, b, c):
    if big(a, b)<c:
        return c
    else:
        return big(a, b)

 print(bigger(10, 20, 30))
except:
   print('Sorry there is an error!')

raw_data = [10, None, 20, 30, None, 40, 50]
cleaned_data = [value for value in raw_data if value is not None]
print(cleaned_data)

calculate_mean = int(sum(cleaned_data)) / len(cleaned_data)
print(calculate_mean)

normalized_data = [value / calculate_mean for value in cleaned_data]
print(normalized_data)


f = open('testfile.txt')
print(f.read())
f.close()

with open('testfile.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)



with open('testfile.txt', 'r') as f:
        size = 10
        content = f.read(size)
        while len(content) > 0:
            print(content, end='#')
            content = f.read(size)
"""
with open('students.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        name, marks = line.strip().split(',')
        if name == "name":
            continue
        print(f"Student: {name}, Score: {marks}")
mean = sum([int(line.strip().split(',')[1]) for line in lines if line.strip().split(',')[0] != "name"]) / (len(lines) - 1)
print(f"Average Score: {mean}")