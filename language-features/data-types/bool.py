# declaration
is_python_course = True
is_csharp_course = False

print (is_python_course is True)
print (is_csharp_course is True)

# Truthy Falsy Check

# Any value other than integer 0 (including negative value) is Truthy
print("Integer 1 boolean value = {}".format(bool(1)))
print("Negative integer 1 boolean value = {}".format(bool(-1)))
print("Float boolean value = {}".format(bool(1.23)))
print("Zero boolean value = {}".format(bool(0)))

# Empty string boolean conversion returns false
print("Non empty string boolean value = {}".format(bool('PYTHON')))
print("Non empty string with space boolean value = {}".format(bool(' ')))
print("Empty string boolean value = {}".format(bool('')))

# Any empty collection is treated as Falsy
print("Empty collection bool value = {}".format(bool([])))
print("Filled collection bool value = {}".format(bool([1, 2, 3])))
