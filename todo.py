# todo.py

TASKS_FILE = "tasks.txt"

# Load tasks from file at start
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n==== TO-DO LIST APP ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove!")
        return
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
