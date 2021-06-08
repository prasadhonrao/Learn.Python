students = []

class Student:
    # class attributes which is shared across all instances
    school_name = "Kennedy Park International"

    # constructor
    def __init__(self, name, id=0):
        self._name = name
        self._id = id
        students.append(self)

    # override toString
    def __str__(self):
        return "Student " + self._name.capitalize()

    def get_school_name(self):
        return Student.school_name

print(Student.school_name)
mark = Student("Mark")
print(mark.get_school_name())