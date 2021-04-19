sum = 0 
for i in range(0, 10):
    if i % 2 == 0:
        sum = sum + i

print(sum)

# Another approach using range step
sum = 0 
for i in range(0, 10, 2):
    sum = sum + i

print(sum)