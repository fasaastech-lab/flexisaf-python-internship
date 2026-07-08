# CLI To-Do List App fuctions

def add_task(tasks, task):
    # Add tasks
    tasks.append([task, "Pending"])
    print("Task was added")


def view_task(tasks):
    # Display tasks
    if not tasks:
        print("No added task yet")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task[0]} - {task[1]}")


def mark_done(tasks, num):
    # Mark tasks as done
    if not (1 <= num <= len(tasks)):
        print("Invalid task number")
    else:
        tasks[num - 1][1] = "Done"
        print("Task is done")
        

def delete_task(tasks, num):
    # Delete tasks
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Tasks deleted")
    else:
        print("Invalid task number")