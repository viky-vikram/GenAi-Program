students = {}

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("\nStudent Grades:")
        for name, marks in students.items():
            grade = calculate_grade(marks)
            print(f"{name} - Marks: {marks}, Grade: {grade}")

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        marks = students[name]
        print(f"{name} - Marks: {marks}, Grade: {calculate_grade(marks)}")
    else:
        print("Student not found.")

def main():
    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

main()