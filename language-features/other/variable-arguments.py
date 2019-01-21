def add_numbers(*args):
    total = 0
    for a in args:
        total = total + a
    return total

print(add_numbers(1))
print(add_numbers(1, 2, 3))
