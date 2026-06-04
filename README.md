# FlexiSAF Python Internship — Beginner Stage

## Project Context
Deliverables for the FlexiSAF Python Programming Internship (Beginner Stage)

## Requirements
- Python 3.6 or higher
- No external libraries required. Uses only Python built-in modules.

## Clone the Repository

```bash
git clone git@github.com:fasaastech-lab/flexisaf-python-internship.git
cd flexisaf-python-internship
```

---

## Week 1: Interactive User Profile Collector

### Description
Collects a user's profile interactively, validates each input, saves it to a JSON file, and reads it back to the user.

### How to Run

```bash
python week1_deliverables.py
```

### Sample Output
Enter your name: Abdulraheem
Enter your age: 31
Enter your email: fasaastech@gmail.com
Enter your phone: 09012981955
Profile saved to profile.json
Saved Profile:
Name: Abdulraheem
Age: 31
Email: fasaastech@gmail.com
Phone: 09012981955

---

## Week 2: Student Grade Calculator

### Description
Accepts a student's assignment, test, and exam scores, calculates the total and average, evaluates pass or fail status, and checks award eligibility.

### How to Run

```bash
python week2_deliverables.py
```

### Sample Output
Enter your assignment score: 18
Enter your test score: 17
Enter your exam score: 55
Assignment score: 18
Test score: 17
Exam score: 55
Total: 90
Average: 30.0
You passed
You qualify for an award


## Week 3: Control Flow

### 3a: Age Validator and Login Flow

#### Description
Age Validator: Collects user age and displays age category.
Login Flow: Stores and verifies user login credentials then grants or denies access.

#### How to Run
```bash
python week3_deliverables.py
```

#### Sample Output
```
Enter your age: 13
You are a teenager
Enter your username: fastmode
Enter your password: 12345
Access granted
```

---

### 3b: Loan Eligibility Checker

#### Description
Collects user age and monthly income, checks eligibility, then evaluates if the loan amount is within repayment range.

#### How to Run
```bash
python week3_loan_eligibility.py
```

#### Sample Output
```
Enter your age: 19
Enter your monthly income: 24356
How much loan do you want: 
Enter loan amount: 30000
Loan request granted
```

---

### 3c: Expense Tracker

#### Description
Collects monthly budget and expenses, calculates total and balance, then flags overspending if expenses exceed the budget.

#### How to Run
```bash
python week3_expense_tracker.py
```

#### Sample Output
```
Enter your monthly budget: 50000
Enter your food expenses: 24000
Enter your transport expenses: 18000
Enter your utilities expenses: 15000
Total expenses: 57000.0
Balance: -7000.0
You're spending above your budget
```