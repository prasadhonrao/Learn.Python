"""
    Python program to accept user input and display customized message
"""

user_name = input('Enter your name : ')
print('You have entered : %s' % user_name)
print('1. Hi {}'.format(user_name))
print('2. Hi {0}'.format(user_name))
print(f'3. Hi {user_name}')
