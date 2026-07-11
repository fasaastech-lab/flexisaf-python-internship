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