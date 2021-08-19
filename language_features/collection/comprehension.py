numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print n from n using for
my_list = []
for n in numbers:
    my_list.append(n)
print(my_list)

# using comprehension
my_list = [n for n in numbers]
print(my_list)

#----------------------------------#

# print n from n using for
my_list = []
for n in numbers:
    my_list.append(n * n)
print(my_list)

# using comprehension
my_list = [n * n for n in numbers]
print(my_list)

#----------------------------------#

# print n from n if n is even using for loop
my_list = []
for n in numbers:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# using comprehension
my_list = [n for n in numbers if n % 2 == 0]
print(my_list)

#----------------------------------#
# print a pair for each letter in word 'abcd' with each letter in '0123' using for loop
my_list = [] 
for letter in 'abcd':
    for number in range(4):
        my_list.append((letter, number))

print(my_list)

# using comprehension
my_list = [(l, n) for l in 'abcd' for n in range(4)]
print(my_list)

#----------------------------------#

# set comprehension
duplicate_numbers = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10]

# print unique n from n using for loop
my_set = set()
for n in duplicate_numbers:
    my_set.add(n)
print(my_set)

# using comprehension
my_set = { n for n in duplicate_numbers }
print(my_set)
