"""
Task List Program
------------------
Why it matters: This teaches how to store multiple items in a single
variable (a list) — the same foundational idea behind databases, which
store many rows of data in one structure.

Key Skill: Lists — using .append() to add items, and a for-loop to print them.
"""

def show_menu():
    print("\n--- TASK LIST MENU ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Exit")


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)          # <-- storing a new item in the list
        print(f'Added: "{task}"')
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):   # <-- print loop
        print(f"{index}. {task}")


def main():
    tasks = []   # a single variable holding many items

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
