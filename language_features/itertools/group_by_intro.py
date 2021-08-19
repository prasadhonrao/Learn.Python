# groupby is a function that groups elements of an iterable into sub-iterables based on a key function.

from itertools import groupby

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def smaller_than_3(x):
    return x < 3

group = groupby(a, key=smaller_than_3)

for k, v in group:
    print(k, list(v))

# using lambdas

group = groupby(a, key=lambda x: x < 5)

for k, v in group:
    print(k, list(v))