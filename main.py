from core_logic import SystemManagement
from database import create_table
from messages import MESSAGES
import helpers

create_table()

system = SystemManagement()


def main():

    while True:

        print("\n=== student management system ===")
        print("1. add student")
        print("2. show students")
        print("3. update student")
        print("4. search student")
        print("5. delete student")
        print("6. add course")
        print("7. show courses")
        print("8. update course")
        print("9. search course")
        print("10. delete course")
        print("11. enroll student")
        print("12. unenroll student")
        print("13. show student's courses")
        print("14. show course's students")
        print("15. exit")

        choice = helpers.get_choice("choose: ")

        if choice == "1":

            name = helpers.get_text_input(
                "student's name: ",
                "this field is required!"
            )

            class_name = helpers.get_text_input(
                "class name: ",
                "this field is required!"
            )
            success = system.add_student(name, class_name)

            if not success:
                print(MESSAGES["student_exists"])
            else:
                print(MESSAGES["student_added"])

        elif choice == "2":
            students = system.get_students()

            if students:
                for student in students:
                    print(student)
            else:
                print(MESSAGES["student_not_found"])

        elif choice == "3":
            student_id = helpers.get_int_input("student's id: ")
            name = helpers.get_text_input("new name: ")
            class_name = helpers.get_text_input("new class name: ")

            success = system.update_student(student_id, name, class_name)

            if success is True:
                print(MESSAGES["student_updated"])

            elif success == "exists":
                print(MESSAGES["student_exists"])

            elif success == "not_found":
                print(MESSAGES["student_not_found"])

            elif success == "no_change":
                print(MESSAGES["no_change"])

        elif choice == "4":
            keyword = helpers.get_search_input("search: ")

            result = system.search_student(keyword)

            if result:

                for item in result:
                    print(item)
            else:
                print(MESSAGES["student_not_found"])

        elif choice == "5":

            student_id = helpers.get_int_input("enter student's id to delete: ")

            success = system.delete_student(student_id)

            if success:
                print(MESSAGES["student_deleted"])
            else:
                print(MESSAGES["student_not_found"])

        elif choice == "6":
            course_name = helpers.get_text_input(
                "course's name: ",
                "this field is required!"
            )

            teacher_name = helpers.get_text_input(
                "teacher's name: ",
                "this field is required!"
            )

            success = system.add_course(course_name, teacher_name)

            if not success:
                print(MESSAGES["course_exists"])

            else:
                print(MESSAGES["course_added"])

        elif choice == "7":

            courses = system.get_courses()

            if courses:
                for course in courses:
                    print(course)
            else:
                print(MESSAGES["course_not_found"])

        elif choice == "8":
            course_id = helpers.get_int_input("course's id: ")
            name = helpers.get_text_input("new name: ")
            teacher = helpers.get_text_input("new teacher's name: ")

            success = system.update_course(course_id, name, teacher)

            if success is True:
                print(MESSAGES["course_updated"])
            
            elif success == "exists":
                print(MESSAGES["course_exists"])

            elif success == "not_found":
                print(MESSAGES["course_not_found"])

            elif success == "no_change":
                print(MESSAGES["no_change"])

        elif choice == "9":
            keyword = helpers.get_search_input("search: ")

            result = system.search_course(keyword)

            if result:

                for item in result:
                    print(item)

            else:
                print(MESSAGES["course_not_found"])

        elif choice == "10":
            course_id = helpers.get_int_input("enter course's id to delete: ")

            success = system.delete_course(course_id)

            if success:
                print(MESSAGES["course_deleted"])
            else:
                print(MESSAGES["course_not_found"])

        elif choice == "11":
            student_id = helpers.get_int_input("student's id: ")
            course_id = helpers.get_int_input("course's id: ")

            result = system.enroll_student(student_id, course_id)

            if result == "student_not_found":
                print(MESSAGES["student_not_found"])

            elif result == "course_not_found":
                print(MESSAGES["course_not_found"])

            elif result == "already_enrolled":
                print(MESSAGES["student_already_enrolled"])

            else:
                print(MESSAGES["student_enrolled"])

        elif choice == "12":
            student_id = helpers.get_int_input("student's id: ")
            course_id = helpers.get_int_input("course's id: ")

            result = system.unenroll_student(student_id, course_id)

            if result == "student_not_found":
                print(MESSAGES["student_not_found"])

            elif result == "course_not_found":
                print(MESSAGES["course_not_found"])

            elif result == "not_enrolled":
                print(MESSAGES["student_not_enrolled"])

            else:
                print(MESSAGES["student_unenrolled"])

        elif choice == "13":
            student_id = helpers.get_int_input("enter student's id: ")

            student = system.get_student_by_id(student_id)

            if not student:
                print(MESSAGES["student_not_found"])

            else:
                courses = system.get_student_courses(student_id)

                if courses:
                    print(f"student {student.id} - {student.name} enrolled in:")

                    for course in courses:
                        print(course)

                else:
                    print(f"student {student.id} - {student.name} not enrolled any course!")

        elif choice == "14":
            course_id = helpers.get_int_input("enter course's id: ")

            course = system.get_course_by_id(course_id)

            if not course:
                print(MESSAGES["course_not_found"])

            else:
                students = system.get_course_students(course_id)

                if students:
                    print(f"course {course.id} - {course.name} has:")

                    for student in students:
                        print(student)
                else:
                    print(f"course {course.id} - {course.name} has no enrolled student!")

        elif choice == "15":
            print("exited!")
            break


if __name__ == "__main__":
    main()
    
    