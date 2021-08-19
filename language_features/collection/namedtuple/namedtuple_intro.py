# namedtuple is a factory function that creates a new subclass of tuple. It is commonly used to create new types that are more efficient than using the built-in tuple type.

from collections import namedtuple

Person = namedtuple('Person', 'name age gender')
print('Type of Person:', type(Person))

bob = Person(name='Bob', age=30, gender='male')
print('Representation:', bob)

jane = Person(name='Jane', age=29, gender='female')
print('Field by name:', jane.name)

print('Fields by index:')
for p in [ bob, jane ]:
    print('%s is a %d year old %s' % p)