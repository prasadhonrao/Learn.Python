# Change case
message = 'Python is fun to learn and I am sure you will enjoy it as well'
print(message.capitalize())
print(message.lower())
print(message.upper())

# Format
print("My full name is {0} {1}".format('Prasad', 'Honrao'))
print("My full name is {firstname} {lastname}".format(firstname = 'Prasad', lastname = 'Honrao'))

# Join 
print ('*'.join(['1', '2', '3', '4', '5']))

# Partition -> Returns 3 part string seperated by seperator. It returns a tuple.
print("unforgettable".partition("forget"))

# replace - replace string and return a new string
old_message = 'This is an old message'
new_message = old_message.replace('old','new')
print(old_message)
print(new_message)

# Slice : Slicing is a way to extract a substring from a string.
s = "Python is extremely powerful language".split()
print(s[0])
print(s[1:4])
print(s[1:-1])
print(s[2:])
print(s[:2])

# Split : Separate string based on seperator and return a list
s = "Python is extremely powerful language".split()
print(s)

# Strip : Remove leading and trailing whitespace
s = "   Python   is   extremely   powerful   language   "
print(s)
print(s.strip())

# creating a copy of string
s1 = s[:] 
print(s1)
