# Counter collection has almost similar APIs as dict, and can be used as a replacement to it

from collections import Counter

# empty counter
c = Counter()

c["apples"] += 1
c["bananas"] += 10
c["apples"] += 5
c["cherries"] += 2

print(c.most_common()) # displays items with sorted list of its count
print(c['lemons']) # default to 0 if element doesn't exists

# counter initialization using list
fruits = ['apple', 'banana', 'cherries', 'mango']
fruits_counter = Counter(fruits)

for item in fruits_counter.elements():
    print(item)


# counter initialization using str
random_string = 'aabbccccddef'
random_string_counter = Counter(random_string)
print(random_string_counter)
print(random_string_counter.keys()) # returns list of keys
print(random_string_counter.values()) # returns list of values
print(random_string_counter.elements()) # returns list of elements
print(random_string_counter.most_common(2)) # most_common(n) returns n most common elements