# deque is a double-ended queue. It is commonly used to implement stacks and queues.
# It is a thread-safe data structure. It supports all the usual queue operations like enqueue, dequeue, isEmpty, size, etc.

from collections import deque

d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('d:', d)

d.appendleft('task0')
print('d:', d)

d.pop()
print('d:', d)

d.popleft()
print('d:', d)

d.clear()
print('d:', d)

d.extend([1, 2, 3, 4])
print('d:', d)

d.extendleft([0])
print('d:', d)

