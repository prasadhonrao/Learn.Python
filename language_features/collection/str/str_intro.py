# strings are immutable sequence of characters

# Declaration using single quote
message = 'Hello, Python World!'
print(message)

# Declaration using double quote
message = "Hello, Python World!"
print(message)

# Declaration and concatenation
message = 'python ' + 'language 1'
print(message)

# Declaration and concatenation
message = 'python ' 'language 2'
print(message)

# Declaration and concatenation on separate line
message = 'python '
message += 'language 3'
print(message)

# Multiline string using '''
message = '''python
           language 4'''
print(message)

# Adding escape sequence
escape = 'Escape Sequence Character \' !!!'
print(escape)

# for path variables
systemPath = r'c:\Windows\System32' # r prefix indicates raw string
print(systemPath)