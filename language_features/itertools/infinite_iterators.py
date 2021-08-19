# count return a generator that counts from 0 to infinity
from itertools import count
for i in count(3):
    print(i)
    if i >= 10:
        break

# cycle returns an iterator that repeats the values infinitely

from itertools import cycle
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in cycle(a):
    print(i)
    if i >= 5:
        break

# repeat returns an iterator that repeats the value infinitely
from itertools import repeat
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in repeat(a, 5):
    print(i)

