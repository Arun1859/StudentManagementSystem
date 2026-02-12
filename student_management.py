import os


class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def to_file_format(self):
        return f"{self.roll},{self.name},{self.marks}\n"


class StudentManagementSystem:

    def __init__(self):
        self.students = {}
        self.file_name = "students.txt"
        self.load_data()

        # Load data from file
    def load_data(self):
        if not os.path.exists(self.file_name):
            print("No previous data found. Starting fresh.")
            return

        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    roll, name, marks = line.strip().split(",")
                    self.students[int(roll)] = Student(
                        int(roll), name, float(marks)
                    )
                    print("Data loaded successfully.")

        except Exception as e:
            print("Error loading file:", e)

            # Save data to file
    def save_data(self):
        try:
            with open(self.file_name, "w") as file:
                for student in self.students.values():
                    file.write(student.to_file_format())

                    print("Data saved successfully.")

        except Exception as e:
            print("Error saving file:", e)

            # Add student
    def add_student(self):
        try:
            roll = int(input("Enter Roll Number: "))

            if roll in self.students:
                print("Student already exists")
                return

            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))

            self.students[roll] = Student(roll, name, marks)

            print("Student added successfully.")

        except ValueError:
            print("Invalid input. Please enter correct data.")

            # View students
    def view_students(self):
        if not self.students:
            print("No students found")
            return

        print("\n*** Students List ***")
        for student in self.students.values():
            print(
                f"Roll: {student.roll}, Name: {student.name}, Marks: {student.marks}"
            )

            # Search student
    def search_student(self):
        try:
            roll = int(input("Enter Roll Number to search: "))

            if roll in self.students:
                student = self.students[roll]
                print(f"Name: {student.name}")
                print(f"Marks: {student.marks}")
            else:
                print("Student not found.")

        except ValueError:
            print("Invalid roll number.")

            # Update marks
    def update_marks(self):
        try:
            roll = int(input("Enter Roll Number: "))

            if roll in self.students:
                new_marks = float(input("Enter new marks: "))
                self.students[roll].marks = new_marks
                print("Marks updated successfully.")

            else:
                print("Student not found.")

        except ValueError:
            print("Invalid input.")

            # Delete student
    def delete_student(self):
        try:
            roll = int(input("Enter Roll Number: "))

            if roll in self.students:
                del self.students[roll]
                print("Student deleted successfully.")

            else:
                print("Student not found.")

        except ValueError:
            print("Invalid input.")

            # Menu
    def run(self):

        print("\n***** Student Management System Started *****")

        while True:

            print("\n***** Student Management System *****")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Marks")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_marks()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.save_data()
                print("Exiting program........")
                break

            else:
                print("Invalid choice. Try again.")


                # Run program
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()
