"""
Student management module
"""
students = []


def get_student_title_case() -> str:
    """
    Function to return student name in title case
    :return: student name
    """
    students_title_case = []
    for student in students:
        students_title_case.append(student["name"].title())
    return students_title_case


def print_students_title_case() -> None:
    """
    Function to print student name using title case
    """
    students_title_case = get_student_title_case()
    print(students_title_case)


def add_student(name, stud_id=999):
    """
    Function to add a student in the list
    :param name: student name
    :param stud_id: student id
    """
    student = {"name": name, "id": stud_id}
    students.append(student)
    print("Student count is {0}".format(len(students)))


def save_file(student):
    """
    Function to save student information to the file
    :param student: student info
    """
    try:
        student_file = open("students.txt", "a")
        student_file.write(student + "\n")
        student_file.close()
    except IOError:
        print("Could not save")


def read_file():
    """
    Function to read student information file
    """
    try:
        student_file = open("students.txt", "r")
        for student in student_file.readlines():
            add_student(student)
        student_file.close()
    except IOError:
        print("Could not read")


# ADD NEW STUDENT BLOCK
student_list = get_student_title_case()
add_student("Prasad", "101")

# ADD NEW STUDENT VIA USER INPUT AND DISPLAY THE LIST
student_name = input("Enter student name : ")
student_id = input("Enter student id : ")
add_student(student_name, student_id)

# PRINT STUDENT DETAILS
print_students_title_case()

# USE BELOW CODE BLOCK IF YOU WANT TO ADD NEW STUDENT IN A LOOP
ADD_NEW_STUDENT_FLAG: str = ""
MESSAGE = "Do you want to add new student record?? Press [Y] / [y] to continue."
ADD_NEW_STUDENT_FLAG = input(MESSAGE)

while ADD_NEW_STUDENT_FLAG in ("Y", "y"):
    student_name = input("enter student name : ")
    student_id = input("enter student id : ")
    add_student(student_name, student_id)
    ADD_NEW_STUDENT_FLAG = input(MESSAGE)

print_students_title_case()

# READ FROM File
read_file()
print_students_title_case()

# WRITE TO FILE
print("writing to file...")
student_name = input("enter student name : ")
student_id = input("enter student id : ")
add_student(student_name, student_id)
save_file(student_name)
