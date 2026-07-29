# FlexiSAF Python Internship — Beginner Stage

## Project Context
Deliverables for the FlexiSAF Python Programming Internship (Beginner Stage)

## Requirements
- Python 3.6 or higher
- No external libraries required for most weeks
- `requests` library required for Week 8 — install with `pip install requests`

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

## Week 8: Error Handling & Debugging

### Required Libraries
- requests — install with `pip install requests`

### 8a: API Request with Error Handling

#### Description
A script that makes a GET request to a public API and handles common errors including connection failures, timeouts, and HTTP errors using try/except blocks.

#### How to Run
```bash
python week8_api_request.py
```

#### Sample Output
```
Request successful
{'args': {}, 'headers': {'Accept': '*/*', ...}, 'url': 'https://httpbin.org/get'}
```

---

### 8b: File Copy Tool

#### Description
A backup tool that copies content from one file to another. Handles missing source files, permission errors, and prevents accidental overwrites by asking for confirmation.

#### How to Run
```bash
python week8_file_copy.py
```

#### Sample Output
```
Enter source file name: test_source.txt
Enter destination file name: test_dest.txt
File copied from test_source.txt to test_dest.txt successfully.
```

---


## Week 9: File Handling (Text Files / CSV)

### 9a: Student Grade CSV Manager

#### Description
Writes student names and scores to a CSV file, reads it back, calculates the class average, and identifies the top performer. A practical grade management tool for VEA.

#### How to Run
```bash
python week9_csv_grades.py
```

#### Sample Output
```
Grades saved to grades.csv
Class average: 77.8
Top performer: Aisha with 88
```

## Week 10: Modules & Imports

### 10a: Basic Math Operations Calculator

#### Description
A calculator split across two files. The math tools module contains reusable functions for addition, subtraction, multiplication, and division. The app module imports these functions and runs a menu loop where the user chooses an operation and enters two numbers to get the result.

#### How to Run
```bash
python week10_math_app.py
```

#### Sample Output
```
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an operation: 1
Enter a: 10
Enter b: 5
15.0

Choose an operation: 4
Enter a: 2
Enter b: 0
Error: Zero can't be a divisor

Choose an operation: 5
Goodbye!
```

---

## Week 11: Dates, Time & Package Management

### Required Libraries
- `pandas` — install with `pip install pandas`

### 11a: Task Logger & Expense Tracker

#### Description
Collects expenses with category, amount, and note. Automatically timestamps each entry using datetime. Saves all expenses to a CSV file and uses pandas to generate a summary showing total spent and average expense.

#### How to Run
```bash
python week11_expense_logger.py
```

#### Sample Output
```
Category (or exit to stop): food
Amount: 1000
Note: breakfast
Category (or exit to stop): book
Amount: 500
Note: notebook
Category (or exit to stop): exit
Expenses saved to expenses.csv

--- Expense Summary ---
Total spent: 1500.0
Average expense: 750.0
```

---

### 11b: Task Logger & Environment Export

#### Description
Tracks user actions and saves them to a text file with timestamps. Each logged action shows exactly when it was performed. Also exports the full Python environment dependencies using pip freeze.

#### How to Run
```bash
python week11_task_logger.py
```

To export environment dependencies:
```bash
pip freeze > requirements_full.txt
```

#### Sample Output
```
--- Task Logger Started ---
Type 'exit' to stop logging.
Enter an action you performed: Reviewed exam questions
Action logged successfully!
Enter an action you performed: Updated student records
Action logged successfully!
Enter an action you performed: exit
Exiting logger. Check 'task_log.txt' for your history.
```