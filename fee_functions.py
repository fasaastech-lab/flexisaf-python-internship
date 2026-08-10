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

def record_payment(students):
    # Record student payments
    id = input("Enter student's ID")
    if id not in students:
        print("Student not found")
    else:
        amount = float(input("Enter amount paid"))
        date = input("Enter the date of payment")
        students[id]["payments"].append({"amount": amount, "date": date})
        print("Payments added successfully")
        save_data(students)
        

def get_balance(students):
    # Get student balance
    id = input("Enter student's ID")
    if id not in students:
        print("Student not found")
    else:
        total_paid = 0
        for p in students[id]["payments"]:
            total_paid += p["amount"]
        balance = students[id]["total_due"] - students[id][
            "discount"] - total_paid
        print(f"Student: {students[id]['name']}")
        print(f"Total Due: {students[id]['total_due']}")
        print(f"Discount: {students[id]['discount']}")
        print(f"Total Paid: {total_paid}")
        print(f"Balance: {balance}")
        return balance

def search_student(students):
    # Search for existing student
    search_key = input("Search by name or class: ").lower()
    results = []
    for id, info in students.items():
        if search_key in info["name"].lower() or search_key in info["class"].lower():
            results.append((id, info))
    
    if not results:
        print("No student found")
    else:
        for id, info in results:
            print(f"Student ID: {id}")
            print(f"Name: {info['name']}")
            print(f"Class: {info['class']}")
            print(f"Total fees: {info['total_due']}")
            print(f"Discount: {info['discount']}")
            # Calculate total paid and balance
            total_paid = 0
            for p in info["payments"]:
                total_paid += p["amount"]
            balance = info["total_due"] - info["discount"] - total_paid

            print(f"Total paid: {total_paid}")
            print(f"Balance: {balance}")
