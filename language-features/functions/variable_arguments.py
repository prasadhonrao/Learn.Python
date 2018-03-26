# *args is used to pass variable number of arguments during function call
def print_args(name, *args):
    print(name)
    print(args)

print_args("Prasad", "Hello", "World", "01/2/2018", True, None)

# **kwargs is used to pass variable number of arguments during function call, but can only be accessed as dictionary
def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])

var_args(name = "Prasad", description = "37 yr old man", feedback="Python professional", random = None)
