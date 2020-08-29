smallest = None
print("Before:", smallest)
for number in [3, 41, 12, 9, 74, 15]:
    if smallest is None or number < smallest:
        smallest = number
        break
    print("Loop:", number, smallest)
print("Smallest:", smallest)