from timeit import default_timer as timer

my_list = ['P'] * 100000000

# bad way to concatenate strings
start = timer()

my_string = ''
for item in my_list:
    my_string += item

stop = timer()
print(stop - start)

# good way to concatenate strings
start = timer()
my_string = ''.join(my_list)
stop = timer()

print(stop - start)