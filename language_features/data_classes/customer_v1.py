class CustomerV1:

    # constructor
    def __init__(self, name, id = 0, age = 0):
        self.name = name
        self.id = id
        if (age < 0):
            raise ValueError("Age cannot be less than zero".format(age))
        self.age = age


    # override toString
    def __str__(self):
        return "Student {0}'s id is {1} and age is {2}".format(self.name.capitalize(), self.id, self.age)

