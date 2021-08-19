# tuples are immutable sequences of arbitrary objects
# tuples are declared using () and elements are separated using comma

# declare empty tuple
empty = ()
print(type(empty))

# declare tuple using constructor
c = tuple('Prasad')
print (c)

# declare tuple using values
t = ("Prasad", "Honrao", 37, "Pune")
print (t)

# access tuple element using indexer
print('First element in tuple is' , t[0])
print('Last element in tuple is' , t[-1])

# find tuple length using len
print('Tuple length is ', len(t))

# iterate through tuple
for item in t:
    print(item, end=' ')
print('')

# size comparison with list
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print("List size :", sys.getsizeof(my_list), "bytes")
print("Tuple size :", sys.getsizeof(my_tuple), "bytes")