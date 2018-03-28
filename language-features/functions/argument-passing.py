numbers = [1, 2, 3]

def append_list(lst): # pass by reference
    lst.append(4)
    print('Inner List = ', lst)

append_list(numbers)
print('Outer List = ', numbers)

def modify_list(lst):
    lst = [4, 5, 6] # list reinitialization to new values
    print('Inner List = ', lst)

modify_list(numbers)
print('Outer List = ', numbers)
