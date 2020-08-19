import threading

def do_work(val):
    print('Doing some work : ', val)
    print('work completed')
    return

val = 'shopping'
t = threading.Thread(target=do_work, args=(val,))
t.start()
t.join()
print('Main thread completed')
