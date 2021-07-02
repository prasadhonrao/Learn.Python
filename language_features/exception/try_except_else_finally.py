try:
    f = open('exception1.py')
except FileNotFoundError:
    print('File not found')
except Exception:
    print('Something went wrong')
else: # if there is no exception while opening the file, then only this code will execute
    print(f.readlines())
finally:
    print('Ending program')