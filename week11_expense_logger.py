import csv
from datetime import datetime
import pandas as pd

expenses = []

while True:
    category = input("Category (or exit to stop): ")
    if category.lower() == "exit":
        break
    amount = float(input("Amount: "))
    note = input("Note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append([amount, category, note, timestamp])
        
with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Amount", "Category", "Note", "Timestamp"])
    for expense in expenses:
        writer.writerow(expense)
print("Expenses saved to expenses.csv")