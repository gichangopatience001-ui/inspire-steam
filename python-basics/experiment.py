#Name : Patience Mukuhi Gichango 
#Date : 23/02/2026
# Program to show use of objects and classes

class Students:

    def __init__(self, name, national_id, course, phone):
        self.name = name
        self.national_id = national_id
        self.course = course
        self.phone = phone
        self.grade = None  # Grade will be assigned later

    def display_details(self):
        print(f"Name : {self.name}")
        print(f"National id : {self.national_id}")
        print(f"Course : {self.course}")
        print(f"Phone number : {self.phone}")
        print(f"Grade : {self.grade}")
        print(f" - " * 30)

    def update_course_and_grade(self, new_course, grade):
        self.course = new_course
        self.grade = grade
    
students = []

# Register students
s1 = Students("Patience", "12345678", "Computer Science", "0712345678")
s2 = Students("John", "87654321", "Business", "0798765432")

students.append(s1)
students.append(s2)    

for student in students:
    student.display_details()

s1.update_course_and_grade("Software Engineering", "A")
s2.update_course_and_grade("Accounting", "B+")

for student in students:
    student.display_details()

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

# Headings
ws.append(["Name", "National ID", "Course", "Phone", "Grade"])

# Add student data
for student in students:
    ws.append([
        student.name,
        student.national_id,
        student.course,
        student.phone,
        student.grade ])

wb.save("students.xlsx")

print("Data saved to students.xlsx successfully!")