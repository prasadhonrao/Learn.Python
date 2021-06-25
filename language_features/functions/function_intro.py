def add(first, second):
    return first + second

print(add(10, 20))
print(str(add(1, 2)))
print(str(add(1.2, 2.3)))
print(add('news', 'paper'))

# datatype can be specified which gets used only to provide type information in IDE. It does 
# not have any significance in program execution

def add2(first:int, second:int) -> int:
    return first + second

print(add2(10,20))
print(add2('welcome', 'back!')) # although function is expecting int, we are passing str here
