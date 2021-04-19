input_numbers = input('Enter numbers separated by a space : ').split()

max = int(input_numbers[0])
min = int(input_numbers[0])
avg = 0
sum = 0

for i in range(0, len(input_numbers)):
    input_numbers[i] = int(input_numbers[i])
    sum = sum + input_numbers[i]
    
    if input_numbers[i] > max:
        max = input_numbers[i]
    
    if input_numbers[i] < min:
        min = input_numbers[i]

avg = sum / len(input_numbers)

print (max, min, avg)