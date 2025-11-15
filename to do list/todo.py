# todo.py
# Clean To-Do List App (WhatsApp-safe formatted)

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found. Add one using: add <task>\n")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks, text):
    text = text.strip()
    if not text:
        print("Cannot add an empty task.")
        return
    tasks.append(text)
    save_tasks(tasks)
    print(f"Task added: {text}")

def remove_task(tasks, number):
    try:
        index = int(number) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task removed: {removed}")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks(tasks):
    confirm = input("Are you sure you want to clear ALL tasks? (y/n): ").lower()
    if confirm == "y":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Canceled.")

def print_help():
    print("""
Available Commands:
  add <task>         Add a new task
  view               Show all tasks
  remove <number>    Remove a task by number
  clear              Delete all tasks
  help               Show help
  exit               Quit app
""")

def main():
    tasks = load_tasks()
    print("====== TO-DO LIST APP ======")
    print_help()

    while True:
        command = input(">> ").strip()
        if not command:
            continue

        parts = command.split(" ", 1)
        action = parts[0].lower()

        if action == "add":
            if len(parts) == 1:
                print("Usage: add <task description>")
            else:
                add_task(tasks, parts[1])

        elif action == "view":
            show_tasks(tasks)

        elif action == "remove":
            if len(parts) == 1:
                print("Usage: remove <task number>")
            else:
                remove_task(tasks, parts[1])

        elif action == "clear":
            clear_tasks(tasks)

        elif action == "help":
            print_help()

        elif action == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()