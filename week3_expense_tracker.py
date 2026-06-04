# Collect monthly budget and expense inputs
monthly_budget = float(input("Enter your monthly budget: "))
food = float(input("Enter your food expenses: "))
transport = float(input("Enter your transport expenses: "))
utilities = float(input("Enter your utilities expenses: "))
# Sum expenses
total_expenses = food + transport + utilities
print(f"Total expenses: {total_expenses}")
# Comparing budget and expenses
if total_expenses <= monthly_budget:
    print("Your expenses are within budget")
else: 
    print("You're spending above your budget")