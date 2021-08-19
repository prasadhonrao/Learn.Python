# Unordered collection of unique and mutable objects

numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
print(numbers)
print(type(numbers))

emptySet = set() # do not initialize using {}, which actually initializes empty dictionary
print(type(emptySet))
print(set("Hello")) 

for c in numbers:
    print(c) # printing order in set is not fixed

# membership check
print(10 in numbers)
print(100 not in numbers)

# set items are mutable
numbers.clear()
numbers.add(10)
numbers.add(20)
numbers.add(30)
print(numbers)

# remove an element from set
numbers.remove(10)

# remove element which does not exist results in error
try:
    numbers.remove(100)
except KeyError:
    print("KeyError: 100 not found")

# return arbitrary element from set
print(numbers.pop())

# remove an element using discard
numbers.discard(101)

# union, intersection, difference
numbers1 = {10, 20, 30, 40, 50}
numbers2 = {10, 30, 40, 50, 60, 70}
print(numbers1.union(numbers2)) # all elements in either set
print(numbers1.intersection(numbers2)) # elements common to both sets
print(numbers1.difference(numbers2)) # elements in numbers1 but not in numbers2
print(numbers2.difference(numbers1)) # elements in numbers2 but not in numbers1
print(numbers1.symmetric_difference(numbers2)) # elements which are in either set but not in both

import itertools
top5 = itertools.islice({1, 2, 3, 4, 5, 6, 7}, 5)
for c in top5:
    print(c) # printing order in set is not fixed
