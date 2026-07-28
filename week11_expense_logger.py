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
        
