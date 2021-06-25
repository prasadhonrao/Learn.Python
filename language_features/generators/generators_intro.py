def Get123():
    print("Getting value 1")
    yield 1
    print("Getting value 2")
    yield 2
    print("Getting value 3")
    yield 3
    print("No more values")

# all generators are iterators

g = Get123()

print(next(g))
print(next(g))


# for i in Get123():
#     print(i)
