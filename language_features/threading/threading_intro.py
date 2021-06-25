import time

start = time.perf_counter()

def do_something():
    print('sleeping for a second')
    time.sleep(1)
    print('sleeping done')

do_something()
do_something()


finish = time.perf_counter()

print(f'Finished in { round(finish-start, 2) } seconds(s)')
