

def AddTasks(tasks, taskName="No name"):

    task = {"name": taskName, "Done": False}
    tasks.append()
    print(f"The task {taskName} was added successfully.")

    return

def ViewTasks(tasks):
    
    print("\nTasks list:")
    
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["Done"] else " "
        print(f"{index}. [{status}] {task['name']}")

def UpdateName(tasks, index, newName):

    correctIndex = index - 1

    if correctIndex >= 0 and correctIndex < len(tasks):

        tasks[correctIndex]["name"] = newName
        print(f"Task {index} update to {newName}")
    
    else:

        print("invalid index")
    
    return

tasks = []

while True:
    print("\nTasks list manager:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Finish task")
    print("5. Remove completed tasks")
    print("6. Close")

    choice = input("Enter your choice: ")

    if choice == "1":
        taskName = input("Enter the task name: ")
        AddTasks(tasks, taskName = taskName)
    
    elif choice == "2":
        ViewTasks(tasks)

    elif choice == "3":
        ViewTasks(tasks)
        index = int(input("Enter the task index: "))
        newName = input("Enter the new task name: ")
        UpdateName(tasks, index, newName)

    elif choice == "6":
        break

print("Finished manager")