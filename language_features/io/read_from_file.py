emp_file = open("employee.txt", "r")

# check if file is readable
print(emp_file.readable())

# read file line by line
for emp in emp_file.readlines():
    print(emp.upper())

emp_file.close()