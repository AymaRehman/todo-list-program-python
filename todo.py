# todo.py
# Simple To-Do List App

tasks = []

def show_menu():
    print("\n==== TO-DO LIST APP ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_no - 1)
        print(f"Task '{removed}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
