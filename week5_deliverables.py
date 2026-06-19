assignments = []

while True:
    print("\n1. Add assignment")
    print("2. View assignments")
    print("3. Mark as completed")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter assignment: ")
        assignments.append([task, "Pending"])
    elif choice == "2":
        for i in range(len(assignments)):
            print(f"{i+1}. {assignments[i][0]} - {assignments[i][1]}")
    elif choice == "3":
        num = int(input("Enter assignment number to mark complete: "))
        assignments[num-1][1] = "Completed"
    elif choice == "4":
        break