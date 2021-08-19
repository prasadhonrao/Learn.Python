numbers = [1, 2, 3, 4, 5]

for i in numbers:
    if i == 3:
        break
    print(i)
else: # this will only be executed if for loop does not hit break
    print("Done")