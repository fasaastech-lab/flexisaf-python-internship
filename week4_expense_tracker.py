expense = []
while True:
    category = input("Enter category ")
    if category.lower() == 'exit':
        break
    else:
        amount = float(input("Enter amount "))
        note = input("Write a note ")
        date = input("Enter date ") 
        expense.append((amount, category, note, date))
