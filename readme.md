# Modular Student Management System

A modular student management system built with Python, Object-Oriented Programming (OOP), and SQLite.

This project allows users to manage students, courses, and enrollments using a persistent SQLite database.

---

# Features

## Student Management

- Add new students
- Prevent duplicate students
- View all students
- Search students by:
  - ID
  - Name
- Delete students

## Course Management

- Add new courses
- Prevent duplicate courses
- View all courses
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

## Database Integration

- SQLite database storage
- Automatic table creation
- Persistent data between program runs
- Foreign key relationships
- Many-to-many relationship using an enrollments table

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
```

---

# Technologies Used

- Python 3
- SQLite3
- Object-Oriented Programming (OOP)
- Modular Programming

---

# Concepts Practiced

This project was created for practicing:

- Classes and Objects
- Methods
- Modular Design
- Helper Functions
- CRUD Operations
- SQLite Databases
- SQL Queries
- Input Validation
- Database Relationships
- Many-to-Many Relationships
- Foreign Keys
- Clean Project Structure

---

# How to Run

### 1. Clone the repository

```bash
git clone https://github.com/parsa-coder1/modular-student-management-system.git
```

### 2. Open the project folder

```bash
cd modular-student-management-system
```

### 3. Run the program

```bash
python main.py
```

---

# Author

Nasrullah Parsa