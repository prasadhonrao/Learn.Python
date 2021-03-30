languages = ["Python", "Scala", "Haskell", "F#"]

# iterating through collection
for l in languages:
    print(l, end=' ')
print('')    

# iterating through range
for i in range(10): # iterate 10 times from 0 to 9
    print(i, end=' ')
print('')

# iterating through range with start and end values
for i in range(5, 10):
    print(i, end=' ')
print('')


# iterating through range with step parameter
for i in range(10, 20, 2): #start, end, step
    print(i, end=' ')
print('')

# iterating using a _ placeholder
for _ in range(5):
    print('hello')


for _ in range(10):
    if (int(input()) % 7 == 0):
        break