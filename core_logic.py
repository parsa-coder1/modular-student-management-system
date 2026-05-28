from models import Student, Course

import helpers


class SystemManagement:

    def __init__(self):
        self.students = []
        self.courses = []

        self.next_student_id = 1
        self.next_course_id = 1


    def add_student(self, name, class_name):

        for student in self.students:

            if student.name.lower() == name.lower() and student.class_name.lower() == class_name.lower():
                return None

        new_student = Student(self.next_student_id, name, class_name)

        self.students.append(new_student)

        self.next_student_id += 1

        return new_student
    

    def get_students(self):

        return self.students
    

    def search_student(self, keyword: str):

        if keyword.isdigit():
            student = helpers.find_by_id(self.students, int(keyword))

            return [student] if student else []
        
        results = []

        for student in self.students:
            if keyword.lower() in student.name.lower():
                results.append(student)

        return results
    

    def delete_student(self, keyword: str):

        found_student = helpers.find_item(self.students, keyword)

        if not found_student:
            return False
        
        for course in self.courses:
            if found_student in course.students:
                course.students.remove(found_student)
        
        self.students.remove(found_student)

        return True
    

    def add_course(self, course_name, teacher):

        for course in self.courses:

            if course.name.lower() == course_name.lower() and course.teacher.lower() == teacher.lower():
                return None

        new_course = Course(self.next_course_id, course_name, teacher)

        self.courses.append(new_course)

        self.next_course_id += 1

        return new_course
    

    def get_courses(self):

        return self.courses
    

    def search_course(self, keyword: str):

        if keyword.isdigit():
            course = helpers.find_by_id(self.courses, int(keyword))

            return [course] if course else []

        results = []

        for course in self.courses:
            if keyword.lower() in course.name.lower():
                results.append(course)

        return results
    

    def delete_course(self, keyword: str):

        found_course = helpers.find_item(self.courses, keyword)

        if not found_course:
            return False
        
        for student in self.students:
            if found_course in student.courses:
                student.courses.remove(found_course)

        self.courses.remove(found_course)

        return True
    

    def enroll_student(self, student_keyword: str, course_keyword: str):

        student = helpers.find_item(self.students, student_keyword)

        course = helpers.find_item(self.courses, course_keyword)

        if not student or not course:
            return False
        
        if course in student.courses:
            return False
        
        student.courses.append(course)
        course.students.append(student)

        return True
    

    def unenroll_student(self, student_keyword: str, course_keyword: str):

        student = helpers.find_item(self.students, student_keyword)
        course = helpers.find_item(self.courses, course_keyword)

        if not student or not course:
            return False
        
        if course not in student.courses:
            return False
        
        student.courses.remove(course)
        course.students.remove(student)

        return True
    