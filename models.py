class Student:

    def __init__(self, student_id, name, class_name):
        self.id = student_id
        self.name = name
        self.class_name = class_name
        self.courses = []


    def __str__(self):
        return f"{self.id} | {self.name} | {self.class_name}"


class Course:

    def __init__(self, course_id, course_name, teacher_name):
        self.id = course_id
        self.name = course_name
        self.teacher = teacher_name
        self.students = []


    def __str__(self):
        return f"{self.id} | {self.name} | {self.teacher}"