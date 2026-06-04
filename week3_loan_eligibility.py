# Collect applicant age and income
age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income: "))
# Check eligibility based on age and income threshold
if monthly_income < 10000 or age < 18:
    print("You're ineligible to take a loan")
else:
    print("How much loan do you want ")
    # Collect loan amount and evaluate against income limit
    loan_amount = float(input("Enter loan amount: "))
    if loan_amount >= monthly_income * 6:
        print("Your loan request is too high")
    else:
        print("Loan request granted")
