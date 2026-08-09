import json
import csv
from datetime import datetime


def save_data(students, filename="fees.json"):
    # Save students dictionary to JSON file
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)


def load_data(filename="fees.json"):
    # Load students dictionary from JSON file
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def add_student(students):
    # Add student data
    id = input("Enter student's ID")
    name = input("Enter student's name")
    student_class = input("Enter student's class")
    total_fees = float(input("Enter total fees due"))
    discount = float(input("Enter discount if applicable"))
    remark = input("Enter remark")

    if id in students:
        print("This ID already exists")
    else:
        students[id] = {
            "name": name,
            "class": student_class,
            "total_due": total_fees,
            "discount": discount,
            "payments": [],
            "remarks": remark
        }
        save_data(students)
        print(f"Student {name} added successfully.")