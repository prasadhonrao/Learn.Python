# Variable scope follows LEGB rule.
# L - Local
# E - Enclosing
# G - Global
# B - BuiltIn

count = 0

def show_count():
    print("count = ", count)

def set_count(c):
     count = c # assigning to new local count variable

def set_count_global(c):
    global count # assigning to global count variable
    count = c

show_count()
set_count(10)
show_count()

# change global count now

show_count()
set_count_global(100)
show_count()

# enclosing scope
def outer():
    x = 'outer'

    def inner():
        # nonlocal x  # refer to enclosing x variable.
        x = 'inner'
        print(x)
    
    inner()
    print(x)

outer()
