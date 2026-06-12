# Initialize empty list to store expenses
expense = []

# Collect expenses until user types exit
while True:
    category = input("Enter category: ")
    if category.lower() == 'exit':
        break
    else:
        amount = float(input("Enter amount: "))
        note = input("Write a note: ")
        date = input("Enter date: ")
        expense.append((amount, category, note, date))

# Display expense summary
print("=" * 20)
print("SUMMARY")
print("=" * 20)
for entry in expense:
    print(f"Category: {entry[1]}  Amount: {entry[0]}  Note: {entry[2]}  Date: {entry[3]}")

# Calculate and display total
total = sum(entry[0] for entry in expense)
print("=" * 20)
print(f"Total expenses: {total}")