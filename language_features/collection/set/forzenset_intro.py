# forzensets are immutable

numbers = frozenset(range(10))
print(numbers)

# numbers.add(100) # AttributeError: 'frozenset' object has no attribute 'add'