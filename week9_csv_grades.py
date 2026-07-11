import csv

students = [
    ["Abdulraheem", 85],
    ["Fatima", 62],
    ["Ibrahim", 78],
    ["Aisha", 88],
    ["Umar", 76]
]

# Write student data to CSV file
with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Score"])
    for student in students:
        writer.writerow(student)
print("Grades saved to grades.csv")

# Read CSV file and calculate average and top performer
with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    
    total = 0
    count = 0
    top_student = ""
    top_score = 0
    
    for row in reader:
        name = row[0]
        score = int(row[1])
        total += score
        count += 1
        if score > top_score:
            top_score = score
            top_student = name

average = total / count
print(f"Class average: {average}")
print(f"Top performer: {top_student} with {top_score}")