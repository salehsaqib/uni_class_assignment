# Base Class University
class University:
    def __init__(self):
        self.students = []  # List to store students
        self.teachers = []  # List to store teachers

# Class Human inheriting from University
class Human(University):
    def __init__(self, name, age):
        super().__init__()  # Inheriting University class
        self.name = name
        self.age = age

# Child class Student inheriting from Human
class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        # Add the student to the students list in the University class
        self.students.append(self)

    def __repr__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, ID: {self.student_id})"

# Child class Teacher inheriting from Human
class Teacher(Human):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        # Add the teacher to the teachers list in the University class
        self.teachers.append(self)

    def __repr__(self):
        return f"Teacher(Name: {self.name}, Age: {self.age}, ID: {self.teacher_id})"

# Class representing a class section
class ClassSection:
    def __init__(self, section_name, class_timings, class_teacher):
        self.section_name = section_name
        self.class_timings = class_timings
        self.class_teacher = class_teacher
        self.students_in_section = []

    def add_student_to_section(self, student):
        self.students_in_section.append(student)

    def __repr__(self):
        return (f"Class Section: {self.section_name}, Timings: {self.class_timings}, "
                f"Teacher: {self.class_teacher}, Students: {[student.name for student in self.students_in_section]}")

# Creating some teacher objects
teacher1 = Teacher("Zia Khan", 60, "MS")
teacher2 = Teacher("Naveed Rana", 35, "BS")
teacher2 = Teacher("Abu Huraira", 25, "BS AI")

# Creating some student objects
student1 = Student("Saleh Saqib", 40, "st-2024=005")
student2 = Student("Sarim", 21, "st-2022=009")
student3 = Student("Arham", 22, "st-2023=008")

# Creating a class section
section_a = ClassSection("Section A", "9:00 AM - 11:00 AM", teacher1)

# Adding students to the section
section_a.add_student_to_section(student1)
section_a.add_student_to_section(student2)

# Print details of the section
print(section_a)

# Display list of students and teachers in the university
print("Students in University:", teacher1.students)
print("Teachers in University:", teacher1.teachers)
