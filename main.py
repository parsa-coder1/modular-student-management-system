from core_logic import SystemManagement

import helpers

system = SystemManagement()


def main():

    while True:

        print("\n=== student management system ===")
        print("1. add student")
        print("2. show students")
        print("3. search student")
        print("4. delete student")
        print("5. add course")
        print("6. show courses")
        print("7. search course")
        print("8. delete course")
        print("9. enroll student")
        print("10. unenroll student")
        print("11. exit")

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
            student = system.add_student(name, class_name)

            if not student:
                print("this student already exists!")
            else:
                print("student added!")

        elif choice == "2":
            students = system.get_students()

            if students:
                for student in students:
                    print(student)
            else:
                print("no student found!")

        elif choice == "3":
            keyword = helpers.get_search_input("search: ")

            result = system.search_student(keyword)

            if result:

                for item in result:
                    print(item)
            else:
                print("no student found!")

        elif choice == "4":

            keyword = helpers.get_search_input("enter student's id or name to delete: ")

            success = system.delete_student(keyword)

            if success:
                print("student deleted successfully!")
            else:
                print("no student found!")

        elif choice == "5":
            course_name = helpers.get_text_input(
                "course's name: ",
                "this field is required!"
            )

            teacher_name = helpers.get_text_input(
                "teacher's name: ",
                "this field is required!"
            )

            course = system.add_course(course_name, teacher_name)

            if not course:
                print("this course already exists!")

            else:
                print("course added successfully!")

        elif choice == "6":

            courses = system.get_courses()

            if courses:
                for course in courses:
                    print(course)
            else:
                print("no course found!")

        elif choice == "7":

            keyword = helpers.get_search_input("search: ")

            result = system.search_course(keyword)

            if result:

                for item in result:
                    print(item)

            else:
                print("no course found!")

        elif choice == "8":

            keyword = helpers.get_search_input("enter course's id/name to delete: ")

            success = system.delete_course(keyword)

            if success:
                print("course deleted successfully!")
            else:
                print("no course found!")

        elif choice == "9":

            s_keyword = helpers.get_search_input("student's id/name: ")
            c_keyword = helpers.get_search_input("course's id/name: ")

            success = system.enroll_student(s_keyword, c_keyword)

            print("enrolled!" if success else "failed!")

        elif choice == "10":

            s_keyword = helpers.get_search_input("student's id/name: ")
            c_keyword = helpers.get_search_input("course's id/name: ")

            success = system.unenroll_student(s_keyword, c_keyword)

            print("unenrolled!" if success else "failed!")

        elif choice == "11":
            print("exited!")
            break


if __name__ == "__main__":
    main()
    