def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

lst = [1, 2, 3, 4, 5]
print(first(lst))

empty_set = set()
print(first(empty_set))