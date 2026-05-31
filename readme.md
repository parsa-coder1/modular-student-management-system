# Modular Student Management System

A modular student management system built with Python, Object-Oriented Programming (OOP), and SQLite.

This project demonstrates how to build a fully functional CRUD system with persistent database storage and many-to-many relationships using SQLite.

---

# Features

## Student Management
- Add new students
- Prevent duplicate students
- View all students
- Update student information
- Search students by:
  - ID
  - Name
- Delete students

## Course Management
- Add new courses
- Prevent duplicate courses
- View all courses
- Update course information
- Search courses by:
  - ID
  - Name
- Delete courses

## Enrollment System
- Enroll students into courses
- Prevent duplicate enrollments
- Unenroll students from courses
- View all courses of a student
- View all students enrolled in a course

---

## Database Integration

- SQLite database storage
- Automatic table creation on startup
- Persistent data between runs
- Foreign key relationships
- Many-to-many relationship using a junction table (`enrollments`)

---

# Project Structure

```text
project/
│
├── main.py
├── core_logic.py
├── models.py
├── helpers.py
├── database.py
├── .gitignore
└── README.md 

Technologies Used
• 
Python 3
• 
SQLite3
• 
Object-Oriented Programming (OOP)
• 
Modular Programming
• 
SQL (DDL & DML)
 
Concepts Practiced
This project was built to practice:
• 
Classes and Objects
• 
Methods and Modules
• 
CRUD Operations
• 
SQLite Database Design
• 
JOIN Queries
• 
Many-to-Many Relationships
• 
Foreign Keys
• 
Input Validation
• 
Clean Architecture
• 
Separation of Concerns
 
How to Run
1. Clone the repository
Bash
git clone https://github.com/parsa-coder1/modular-student-management-system.git
2. Enter project folder
Bash
cd modular-student-management-system
3. Run the program
Bash
python main.py
 
Author
Nasrullah Parsa