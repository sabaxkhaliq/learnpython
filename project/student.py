import json

FILE_NAME = "student.json"

students_grade = {}


def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_student(name, grade):
    students_grade[name] = grade
    save_data(students_grade)
    print(f"{name} added successfully")


def update_student(name, grade):
    if name in students_grade:
        students_grade[name] = grade
        save_data(students_grade)
        print(f"{name} updated successfully")
    else:
        print("Student not found")


def delete_student(name):
    if name in students_grade:
        del students_grade[name]
        save_data(students_grade)
        print(f"{name} deleted successfully")
    else:
        print("Student not found")


def view_students():
    if students_grade:
        for name, grade in students_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No students found")


def main():

    global students_grade
    students_grade = load_data()

    while True:
        print("1.Add Student")
        print("2.Update Student")
        print("3.Delete Student")
        print("4.View Students")
        print("5.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            grade = input("Enter grade: ")
            add_student(name, grade)

        elif choice == "2":
            name = input("Enter name: ")
            grade = input("Enter new grade: ")
            update_student(name, grade)

        elif choice == "3":
            name = input("Enter name: ")
            delete_student(name)

        elif choice == "4":
            view_students()

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()