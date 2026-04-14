from database import engine, SessionLocal
from models import Base, Student

Base.metadata.create_all(bind=engine)

session = SessionLocal()

def create_student():
    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")

    student = Student(name=name, age=age, course=course)
    session.add(student)
    session.commit()
    print("Student added!")

def show_students():
    students = session.query(Student).all()
    for s in students:
        print(s)

def update_student():
    student_id = int(input("Enter ID: "))
    student = session.query(Student).get(student_id)

    if student:
        student.name = input("New name: ")
        student.age = int(input("New age: "))
        student.course = input("New course: ")
        session.commit()
        print("Updated!")
    else:
        print("Not found")

def delete_student():
    student_id = int(input("Enter ID: "))
    student = session.query(Student).get(student_id)

    if student:
        session.delete(student)
        session.commit()
        print("Deleted!")
    else:
        print("Not found")

while True:
    print("\n1. Add student")
    print("2. Show students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")