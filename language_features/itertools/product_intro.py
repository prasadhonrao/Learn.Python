# product is a generator that returns all possible combinations of the elements in the iterables
# product(A, B) returns the same as ((x,y) for x in A for y in B)

from itertools import product

a = [1, 2]
b = [3, 4]

prod = product(a, b)
print(list(prod))