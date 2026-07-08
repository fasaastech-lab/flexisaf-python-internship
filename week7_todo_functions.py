def add_task(tasks, task):
    tasks.append([task, "Pending"])
    print("Task was added")


def view_task(tasks):
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")



    