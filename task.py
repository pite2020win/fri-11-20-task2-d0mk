import logging
from random import choices


class Student:
    ID = 0

    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname
        self.id = Student.ID
        Student.ID += 1

    def __str__(self):
        return f'Student: {self.firstname} {self.surname}, ID = {self.id}'


class Class:
    ID = 0

    def __init__(self, name):
        self.name = name
        self.assigned_students = []
        self.class_dates = []
        self.id = Class.ID
        Class.ID += 1

    def add_students(self, new_students):
        self.assigned_students.extend(new_students)

    def get_student_list(self):
        return self.assigned_students

    def __str__(self):
        return self.name


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.classes = []

    def add_students(self, new_students):
        self.students.extend(new_students)

    def add_classes(self, classes):
        self.classes.extend(classes)

    def get_students(self):
        return self.students

    def get_classes(self):
        return self.classes

    def __str__(self):
        return self.name


def main():
    log = logging.getLogger(__name__)

    number_of_students = 10
    students = (Student(f'Firstname_{n}', f'Surname_{n}') for n in range(number_of_students))

    classes = (
        Class('Math I'),
        Class('Math II'),
        Class('Biology')
    )

    school = School('High School Name')
    school.add_students(students)
    school.add_classes(classes)

    log.info(f'School name: {school}')
    log.info(f'Students: ')


if __name__ == '__main__':
    main()