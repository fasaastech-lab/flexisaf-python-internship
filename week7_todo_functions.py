def add_task(tasks, task):
    tasks.append([task, "Pending"])
    print("Task was added")


def view_task(tasks):
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task[0]} - {task[1]}")


def mark_done(tasks, num):
    tasks[num-1][1] = "Done"
    print("Task is done")
    