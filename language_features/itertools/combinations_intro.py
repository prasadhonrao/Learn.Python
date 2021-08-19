# combinations is a generator that returns combinations of items in a list
# combinations_with_replacement is a generator that returns combinations of items in a list with replacement

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]

comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
