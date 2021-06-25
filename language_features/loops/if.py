"""
    Module to explain if-else condition in Python
"""

# Simple if - else condition 
number = int(input('Enter any number : '))
if number >= 10:
    print(f"{number} is greater than or equal to 10")
else:
    print(f"{number} is less than 10")

# Multiple if - else condition 
number = int(input('Enter another number : '))
if number >= 100:
    print(f"{number} is greater than or equal to 100")
elif number >= 50:
    print(f"{number} is greater than or equal to 50")
else:
    print(f"{number} is less than 50")

# Truthy Falsy Rule
# 1. Any number other than 0 is true
# 2. Any string other than empty string is true
# 3. None is falsy value

if True:
    print("This will be printed")

if False:
    print("This will not be printed")

if bool(0):
    print("This will not be printed as zero is false")

if bool("0"):
    print("This will be printed as zero is a string here")

if not None:
    print("None is a falsy value")
