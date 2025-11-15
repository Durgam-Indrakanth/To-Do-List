import os

file_name = "tasks.txt"

""" Load & Save Functions """
def load_tasks():
    """ Load tasks from the file """
    if not os.path.exists(file_name):
        return []
    
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    tasks = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        title, status = line.split(" | ")
        tasks.append({"title": title, "completed": status == "completed"})
    return tasks

def save_tasks(tasks):
    """ Save tasks to the file """
    with open(file_name, "w") as file:
        for t in tasks:
            status = "completed" if t["completed"] else "pending"
            file.write(f"{t['title']} | {status}\n")

""" Task Management Functions """
def view_tasks(tasks):
    """ Display all tasks """
    if not tasks:
        print("No tasks found.")
        return
    
    print("Your Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t["completed"] else "✗"
        print(f"{i}. {t['title']} [{status}]")
    print()

def add_task(tasks):
    """ Add a new task """
    title = input("Enter task: ").strip()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added.")

def edit_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid number.")
            return

        new_title = input("New task name: ").strip()
        tasks[index]["title"] = new_title
        save_tasks(tasks)
        print("Task updated.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid number.")
            return

        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    except ValueError:
        print("Enter a valid number.")

def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete/incomplete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid number.")
            return

        tasks[index]["completed"] = not tasks[index]["completed"]
        save_tasks(tasks)
        print("Task updated.")
    except ValueError:
        print("Enter a valid number.")

""" Main Application Loop """
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Update Task (mark complete/incomplete)")
        print("0. Exit")
    
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            update_task(tasks)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()