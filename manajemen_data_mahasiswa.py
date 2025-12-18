"""
Student Management System
An advanced system for managing student data with better structure, features, and design principles.
Built to demonstrate professional-level Python code.

Author: cireng-etc
Date: 2025-12-18
"""

# Import required modules
import os
import json
from dataclasses import dataclass, asdict
from typing import List, Optional

# Define constants for file paths or other configurations
DATA_FILE_PATH = "students_data.json"

def ensure_data_file_exists(path: str):
    """Ensure the data file exists to avoid FileNotFound errors later."""
    if not os.path.exists(path):
        with open(path, 'w') as file:
            json.dump([], file)

# Call the function to ensure system files are in place
ensure_data_file_exists(DATA_FILE_PATH)

@dataclass
class Student:
    """Model representing a single student."""
    id: int
    name: str
    age: int
    gpa: float
    major: str
    email: str

class StudentManager:
    """Core class to handle student management operations."""

    def __init__(self, data_file: str):
        self.data_file = data_file
        self.students = self.load_students()

    def load_students(self) -> List[Student]:
        """Load all students from the storage file."""
        with open(self.data_file, 'r') as file:
            students_data = json.load(file)
            return [Student(**student) for student in students_data]

    def save_students(self):
        """Save all student records back to the file."""
        with open(self.data_file, 'w') as file:
            json.dump([asdict(student) for student in self.students], file, indent=4)

    def add_student(self, name: str, age: int, gpa: float, major: str, email: str) -> Student:
        """Add a new student record."""
        new_id = max([student.id for student in self.students], default=0) + 1
        new_student = Student(id=new_id, name=name, age=age, gpa=gpa, major=major, email=email)
        self.students.append(new_student)
        self.save_students()
        return new_student

    def find_student(self, student_id: int) -> Optional[Student]:
        """Retrieve a single student by their unique ID."""
        return next((student for student in self.students if student.id == student_id), None)

    def remove_student(self, student_id: int) -> bool:
        """Remove a student based on their ID."""
        student_to_remove = self.find_student(student_id)
        if student_to_remove:
            self.students.remove(student_to_remove)
            self.save_students()
            return True
        return False

    def update_student(self, student_id: int, **kwargs) -> Optional[Student]:
        """Update details of an existing student."""
        student = self.find_student(student_id)
        if student:
            for field, value in kwargs.items():
                if hasattr(student, field):
                    setattr(student, field, value)
            self.save_students()
            return student
        return None

    def list_students(self) -> List[Student]:
        """List all registered students."""
        return self.students

    def get_highest_gpa_student(self) -> Optional[Student]:
        """Return the student with the highest GPA."""
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.gpa)

    def get_average_gpa(self) -> float:
        """Calculate the average GPA among students."""
        if not self.students:
            return 0.0
        return sum(student.gpa for student in self.students) / len(self.students)

    def filter_students_by_major(self, major: str) -> List[Student]:
        """Filter students based on their major."""
        return [student for student in self.students if student.major.lower() == major.lower()]

# Code to execute when the file runs directly
if __name__ == "__main__":
    manager = StudentManager(data_file=DATA_FILE_PATH)

    print("Advanced Student Management System\n")
    print("Options:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Update student")
    print("4. Get highest GPA student")
    print("5. Calculate average GPA")
    print("6. List all students")
    print("7. Filter students by major")
    print("8. Exit")

    while True:
        try:
            option = int(input("\nPlease select an option (1-8): "))

            if option == 1:
                name = input("Enter student's name: ")
                age = int(input("Enter student's age: "))
                gpa = float(input("Enter student's GPA: "))
                major = input("Enter student's major: ")
                email = input("Enter student's email: ")
                student = manager.add_student(name=name, age=age, gpa=gpa, major=major, email=email)
                print("\nAdded student:", student)

            elif option == 2:
                student_id = int(input("Enter student ID to remove: "))
                result = manager.remove_student(student_id)
                message = "Student successfully removed." if result else "Student ID not found."
                print(message)

            elif option == 3:
                student_id = int(input("Enter student ID to update: "))
                print("(Leave fields empty to keep current values)")
                updated_fields = {}
                name = input("New name (or old name): ").strip()
                if name:
                    updated_fields['name'] = name
                age = input("New age (or blank): ").strip()
                if age:
                    updated_fields['age'] = int(age)
                gpa = input("New GPA (or blank): ").strip()
                if gpa:
                    updated_fields['gpa'] = float(gpa)
                major = input("New major (or blank): ")
                if major:
                    updated_fields['major'] = major
                email = input("New email (or blank): ")
                if email:
                    updated_fields['email'] = email

                updated_student = manager.update_student(student_id, **updated_fields)
                if updated_student:
                    print("Updated student:", updated_student)
                else:
                    print("Student ID not found.")

            elif option == 4:
                top_student = manager.get_highest_gpa_student()
                print("Highest GPA student:", top_student if top_student else "No students available.")

            elif option == 5:
                avg_gpa = manager.get_average_gpa()
                print(f"Average GPA among students: {avg_gpa:.2f}")

            elif option == 6:
                all_students = manager.list_students()
                print("All registered students:")
                for student in all_students:
                    print(student)

            elif option == 7:
                major = input("Enter the major to filter by: ")
                filtered = manager.filter_students_by_major(major)
                if filtered:
                    print("Filtered students:")
                    for student in filtered:
                        print(student)
                else:
                    print("No students found for the given major.")

            elif option == 8:
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid option, try again.")

        except ValueError:
            print("Invalid input, please try again with correct format.")