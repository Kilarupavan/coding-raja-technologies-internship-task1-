# coding-raja-technologies-internship-task1
import sys

tasks = []

def show_menu():
    print("Command Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

def add_task(task):
    tasks.append({"task": task, "done": False})
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for idx, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx + 1}. {task['task']} - {status}")

def mark_task_done(idx):
    if 1 <= idx <= len(tasks):
        tasks[idx - 1]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid task index.")

def remove_task(idx):
    if 1 <= idx <= len(tasks):
        del tasks[idx - 1]
        print("Task removed.")
    else:
        print("Invalid task index.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            idx = int(input("Enter task index: "))
            mark_task_done(idx)
        elif choice == "4":
            idx = int(input("Enter task index: "))
            remove_task(idx)
        elif choice == "5":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
