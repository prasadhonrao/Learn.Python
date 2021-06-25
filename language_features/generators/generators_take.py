# take 
def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def run_take():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in take(3, items):
        print(item)

run_take()