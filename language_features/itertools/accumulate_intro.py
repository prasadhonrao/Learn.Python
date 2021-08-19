# accumulate is a generator function that returns accumulated sums of the elements of an iterable.
# accumulate(range(5)) = [0, 1, 3, 6, 10]
# accumulate(range(5), operator.mul) = [0, 1, 2, 6, 24]
# accumulate(range(5), operator.mul, 1) = [0, 1, 2, 6, 24]

from itertools import accumulate

a = [1, 2, 3, 4]

acc = accumulate(a)
print(a)
print(list(acc))

import operator

acc = accumulate(a, operator.mul)
print(a)
print(list(acc))