# Import needed functions
from week7_todo_functions import add_task, view_task, mark_done, delete_task

# Create tasks list
tasks = []

# Main menu loop
while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    option = input("Choose an option: ")

    if option == "1":
        task = input("Enter task: ")
        add_task(tasks, task)
    elif option == "2":
        view_task(tasks)
    elif option == "3":
        num = int(input("Enter task number to mark: "))
        mark_done(tasks, num)
    elif option == "4":
        num = int(input("Enter task number to delete: "))
        delete_task(tasks, num)
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Choose a number between 1 and 5")
