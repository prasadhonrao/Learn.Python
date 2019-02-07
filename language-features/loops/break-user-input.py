# Another example to break continuous loop using a condition
while True:
    response = input()
    if (int(response) % 7 == 0):
        break