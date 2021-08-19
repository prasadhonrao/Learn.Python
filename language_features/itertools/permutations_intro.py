# permutations is a generator that yields successive permutations of a sequence.

from itertools import permutations

a = [1, 2, 3]

prod = permutations(a)
print(list(prod))

prod = permutations(a, 2)
print(list(prod))
