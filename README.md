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
## Week 4: Loops

### 4a: Password Strength Checker

#### Description
A console program that asks the user for a password and evaluates its strength by scanning characters and applying rules. Reports Weak, Medium, or Strong with actionable tips.

#### How to Run
```bash
python week4_password_checker.py
```

#### Sample Output
```
Enter password: wert234
Password is weak
Tip: Use at least 8 characters, include numbers and special characters like !@#$.
```

---

### 4b: Expense Tracker with Loop

#### Description
A console loop that repeatedly prompts the user to add expenses including amount, category, note, and date. Stops when the user types exit and displays a full summary with total.

#### How to Run
```bash
python week4_expense_tracker.py
```

#### Sample Output
```
Enter category: Book
Enter amount: 500
Write a note: School notebook
Enter date: 12/06/2026
Enter category: exit
====================
SUMMARY
====================
Category: Book  Amount: 500.0  Note: School notebook  Date: 12/06/2026
====================
Total expenses: 500.0
```

## Week 5: Lists & Tuples

### 5a: To-Do List Manager

#### Description
A console menu program that helps students manage school assignments. Students can add, view, mark as completed, and remove assignments stored in a list of lists.

#### How to Run
```bash
python week5_deliverables.py
```

#### Sample Output
```
1. Add assignment
2. View assignments
3. Mark as completed
4. Remove assignment
5. Exit
Choose an option: 1
Enter assignment: Maths
Choose an option: 1
Enter assignment: English
Choose an option: 2
1. Maths - Pending
2. English - Pending
Choose an option: 3
Enter assignment number to mark complete: 1
Choose an option: 2
1. Maths - Completed
2. English - Pending
Choose an option: 5
```

---

### 5b: Expense Tracker with Tuples

#### Description
Collects daily school-related expenses stored as tuples of item and amount. Uses list comprehension to filter and display expenses above a specified amount.

#### How to Run
```bash
python week5_deliverables.py
```

#### Sample Output
```
Enter expense item (or type exit to stop): Textbook
Enter amount: 3500
Enter expense item (or type exit to stop): Pen
Enter amount: 100
Enter expense item (or type exit to stop): exit

All expenses:
('Textbook', 3500.0)
('Pen', 100.0)

Expenses above 1000:
('Textbook', 3500.0)
```

## Week 6: Dictionaries & Sets

### 6a: Student Contact Manager

#### Description
A console program that stores and manages student, parent, and teacher contact details using nested dictionaries. Uses sets to prevent duplicate emails and phone numbers. Supports adding, viewing, searching, updating, and deleting contacts with input validation.

#### How to Run
```bash
python week6_deliverables.py
```

#### Sample Output
```
1. Add contact
2. View contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit
Choose an option: 1
Enter an ID: S001
Enter your name: Abdulraheem Fasasi
Enter your email: abdulraheem@vea.edu.ng
Enter your phone number: 09012981955
Enter your role: Student
Contact added successfully

Choose an option: 3
Enter contact ID: S001
Name: Abdulraheem Fasasi
Email: abdulraheem@vea.edu.ng
Phone: 09012981955
Role: Student

Choose an option: 6
```

---

## Week 7: Functions, Built-in Functions & Modules

### 7a: CLI To-Do List App

#### Description
A command-line To-Do List application split across two files. The functions module contains reusable functions for adding, viewing, marking, and deleting tasks. The app module imports these functions and runs the menu loop. Uses enumerate() to number tasks and handles invalid input politely.

#### How to Run
```bash
python week7_todo_app.py
```

#### Sample Output
```
1. Add task
2. View tasks
3. Mark task as done
4. Delete task
5. Exit
Choose an option: 1
Enter task: Maths assignment
Task was added

Choose an option: 1
Enter task: English essay
Task was added

Choose an option: 2
1. Maths assignment - Pending
2. English essay - Pending

Choose an option: 3
Enter task number: 1
Task is done

Choose an option: 2
1. Maths assignment - Done
2. English essay - Pending

Choose an option: 4
Enter task number: 2
Tasks deleted

Choose an option: 2
1. Maths assignment - Done

Choose an option: 5
Goodbye!
```