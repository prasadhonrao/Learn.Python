students = []

class Student:

    # initializer
    def __init__(self, name, id = 0, age = 0):
        self.name = name
        self.id = id
        if (age < 0):
            raise ValueError(f"Age cannot be less than zero {age}")
        self._age = age

        students.append(self)

    # override toString
    def __str__(self):
        return "Student {0}'s id is {1} and age is {2}".format(self.name.capitalize(), self.id, self.age)

    # define age property
    def age(self):
        return self.age

mark = Student("mark")
jack = Student("jack", 101, 10) # Change age to -ve to raise an exception

print(mark)
print(jack)