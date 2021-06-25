numbers = [1, 2, 3]

def append_list(lst): # pass by reference
    lst.append(4)
    print('Inner List = ', lst)

append_list(numbers)
print('Outer List = ', numbers)

def modify_list(lst):
    lst = [4, 5, 6] # list re-initialization to new values
    print('Inner List = ', lst)

modify_list(numbers)
print('Outer List = ', numbers)


def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)
