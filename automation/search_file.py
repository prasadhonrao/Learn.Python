import os
filename = input('enter file name to search: ')
for r, d, f in os.walk('/Users/ph'):
    for file in f:
        if file == filename:
            print(os.path.join(r, file))
            exit()