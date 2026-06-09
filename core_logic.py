import sqlite3
from models import Student, Course
from database import connect_db


class SystemManagement:

    def __init__(self):
        pass


    def add_student(self, name, class_name):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id FROM students
        WHERE LOWER(name) = LOWER(?) AND LOWER(class_name) = LOWER(?)
        """, (name, class_name))

        existing_student = cursor.fetchone()

        if existing_student:
            connection.close()
            return False

        cursor.execute("""
        INSERT INTO students (name, class_name)
        VALUES (?, ?)
        """, (name, class_name))

        connection.commit()
        connection.close()

        return True
    

    def get_students(self):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id, name, class_name FROM students
        """)

        rows = cursor.fetchall()

        connection.close()

        students = []

        for row in rows:
            student = Student(row[0], row[1], row[2])
            students.append(student)

        return students
    

    def get_student_by_id(self, student_id):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id, name, class_name FROM students
        WHERE id = ?
        """, (student_id,))

        row = cursor.fetchone()

        connection.close()

        if not row:
            return None
        
        return Student(row[0], row[1], row[2])
    

    def update_student(self, student_id, name, class_name):

        connection = connect_db()
        cursor = connection.cursor()

        student = self.get_student_by_id(student_id)

        if not student:
            connection.close()
            return "not_found"
        
        if student.name.lower() == name.lower() and student.class_name.lower() == class_name.lower():
            connection.close()
            return "no_change"

        cursor.execute("""
        SELECT id FROM students
        WHERE LOWER(name) = LOWER(?) AND LOWER(class_name) = LOWER(?) AND id != ?
        """, (name, class_name, student_id))

        existing_student = cursor.fetchone()

        if existing_student:
            connection.close()
            return "exists"

        cursor.execute("""
        UPDATE students
        SET name = ?, class_name = ?
        WHERE id = ?
        """, (name, class_name, student_id))

        connection.commit()

        success = cursor.rowcount > 0

        connection.close()

        return success
    

    def search_student(self, keyword):

        connection = connect_db()
        cursor = connection.cursor()

        if keyword.isdigit():
            cursor.execute("""
            SELECT id, name, class_name FROM students
            WHERE id = ?
            """, (int(keyword),))

        else:
            cursor.execute("""
            SELECT id, name, class_name FROM students
            WHERE name LIKE ?
            """, (f"%{keyword}%",))

        rows = cursor.fetchall()

        connection.close()

        students = []

        for row in rows:
            student = Student(row[0], row[1], row[2])
            students.append(student)

        return students


    def delete_student(self, student_id):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        DELETE FROM enrollments
        WHERE student_id = ?
        """, (student_id,))

        cursor.execute("""
        DELETE FROM students
        WHERE id = ?
        """, (student_id,))

        connection.commit()

        success = cursor.rowcount > 0

        connection.close()

        return success
 

    def add_course(self, course_name, teacher):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id FROM courses
        WHERE LOWER(name) = LOWER(?) AND LOWER(teacher) = LOWER(?)
        """, (course_name, teacher))

        existing_course = cursor.fetchone()

        if existing_course:
            connection.close()
            return False

        cursor.execute("""
        INSERT INTO courses (name, teacher)
        VALUES (?, ?)
        """, (course_name, teacher))

        connection.commit()
        connection.close()

        return True


    def get_courses(self):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id, name, teacher FROM courses
        """)

        rows = cursor.fetchall()

        connection.close()

        courses = []

        for row in rows:
            course = Course(row[0], row[1], row[2])
            courses.append(course)

        return courses
    

    def get_course_by_id(self, course_id):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id, name, teacher FROM courses
        WHERE id = ?
        """, (course_id,))

        row = cursor.fetchone()

        connection.close()

        if not row:
            return None
        
        return Course(row[0], row[1], row[2])
    

    def update_course(self, course_id, name, teacher):

        connection = connect_db()
        cursor = connection.cursor()

        course = self.get_course_by_id(course_id)

        if not course:
            connection.close()
            return "not_found"
        
        if course.name.lower() == name.lower() and course.teacher.lower() == teacher.lower():
            connection.close()
            return "no_change"
        
        cursor.execute("""
        SELECT id FROM courses
        WHERE LOWER(name) = LOWER(?) AND LOWER(teacher) = LOWER(?) AND id != ?
        """, (name, teacher, course_id))

        existing_course = cursor.fetchone()

        if existing_course:
            connection.close()
            return "exists"
        
        cursor.execute("""
        UPDATE courses
        SET name = ?, teacher = ?
        WHERE id = ?
        """, (name, teacher, course_id))

        connection.commit()

        success = cursor.rowcount > 0

        connection.close()

        return success

    
    def search_course(self, keyword):

        connection = connect_db()
        cursor = connection.cursor()

        if keyword.isdigit():
            cursor.execute("""
            SELECT id, name, teacher FROM courses
            WHERE id = ?
            """, (int(keyword),))

        else:
            cursor.execute("""
            SELECT id, name, teacher FROM courses
            WHERE name LIKE ?
            """, (f"%{keyword}%",))

        rows = cursor.fetchall()

        connection.close()

        courses = []

        for row in rows:
            course = Course(row[0], row[1], row[2])
            courses.append(course)

        return courses


    def delete_course(self, course_id):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        DELETE FROM enrollments
        WHERE course_id = ?
        """, (course_id,))

        cursor.execute("""
        DELETE FROM courses
        WHERE id = ?
        """, (course_id,))

        connection.commit()

        success = cursor.rowcount > 0

        connection.close()

        return success


    def enroll_student(self, student_id, course_id):

        connection = connect_db()
        cursor = connection.cursor()

        try:

            cursor.execute("""
            SELECT id FROM students
            WHERE id = ?
            """, (student_id,))

            if not cursor.fetchone():
                return "student_not_found"
            
            cursor.execute("""
            SELECT id FROM courses
            WHERE id = ?
            """, (course_id,))

            if not cursor.fetchone():
                return "course_not_found"
            
            cursor.execute("""
            SELECT student_id, course_id FROM enrollments
            WHERE student_id = ? AND course_id = ?
            """, (student_id, course_id))

            if cursor.fetchone():
                return "already_enrolled"

            cursor.execute("""
            INSERT INTO enrollments (student_id, course_id)
            values (?, ?)
            """, (student_id, course_id))

            connection.commit()

            return True
        
        except sqlite3.IntegrityError:
            return "already_enrolled"
        
        finally:
            connection.close()
    

    def unenroll_student(self, student_id, course_id):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id FROM students
        WHERE id = ?
        """, (student_id,))

        student = cursor.fetchone()

        if not student:
            connection.close()
            return "student_not_found"
        
        cursor.execute("""
        SELECT id FROM courses
        WHERE id = ?
        """, (course_id,))

        course = cursor.fetchone()

        if not course:
            connection.close()
            return "course_not_found"
        
        cursor.execute("""
        SELECT student_id, course_id FROM enrollments
        WHERE student_id = ? AND course_id = ?
        """, (student_id, course_id))

        exist = cursor.fetchone()

        if not exist:
            connection.close()
            return "not_enrolled"

        cursor.execute("""
        DELETE FROM enrollments
        WHERE student_id = ? AND course_id = ?
        """, (student_id, course_id))

        connection.commit()
        connection.close()

        return True
    

    def get_student_courses(self, student_id):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT courses.id, courses.name, courses.teacher
        FROM courses
        JOIN enrollments
        ON courses.id = enrollments.course_id
        WHERE enrollments.student_id = ?
        """, (student_id,))

        rows = cursor.fetchall()

        connection.close()

        courses = []

        for row in rows:
            course = Course(row[0], row[1], row[2])
            courses.append(course)

        return courses
    

    def get_course_students(self, course_id):

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT students.id, students.name, students.class_name
        FROM students
        JOIN enrollments
        ON students.id = enrollments.student_id
        WHERE enrollments.course_id = ?
        """, (course_id,))

        rows = cursor.fetchall()

        connection.close()

        students = []

        for row in rows:
            student = Student(row[0], row[1], row[2])
            students.append(student)

        return students
        