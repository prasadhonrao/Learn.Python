r = range(5)
print(r)

for i in r:
    print(i, end=' ')
print('\n')

for i in range(5, 10):
    print(i, end=' ')
print('\n')

for i in range(10, 100, 10):
    print(i, end=' ')
print('\n')

# prefer enumerate function to iterate over range, which returns index and value
r = range(0, 100, 10)
for p in enumerate(r):
    print(p, end=' ')
print()

# conver range to list
lst = list(range(5))
print(lst)


    