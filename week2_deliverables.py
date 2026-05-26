# Collect student's result input
assignment = int(input("Enter your assignment score: "))
test = int(input("Enter your test score: "))
exam = int(input("Enter your exam score: "))
# Calculate results and set standards
total = assignment + test + exam
average = total / 3
pass_mark = 50
# Display result
print(f"Assignment score: {assignment}")
print(f"Test score: {test}")
print(f"Exam score: {exam}")
print(f"Total: {total}")
print(f"Average: {average}")
# Evaluate performance to standard
if total >= pass_mark:
    you_pass = True
    print("You passed")
else:
    you_pass = False
    print("You failed")
# Check award eligibility
if total >= 95 and you_pass:
    print("You qualify for an award")
else:
    print("You do not qualify for an award")
