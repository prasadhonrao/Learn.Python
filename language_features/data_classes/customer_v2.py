from dataclasses import dataclass, field
import typing

@dataclass()
class CustomerV2(object):
    id: int
    name: str
    address: str

c =  CustomerV2(1, 'Prasad', 'Pune')
c.id = 2
print(c)

@dataclass(frozen=True)
class CustomerV3(object):
    id: int
    name: str
    address: str

c =  CustomerV3(1, 'Prasad', 'Pune')
c.id = 2
print(c)
