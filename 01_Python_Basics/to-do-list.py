# load exiting items 
#1. Create a new item
#2. List itmes
#3. Mark item as complete
#4. Save items

import json

def load_items():
    pass

def save_items():
    pass

def view_items():
    pass

def create_task():
    pass

def mark_item_complete():
    pass

def main():
    tasks = load_items()

    while True:
        print("\nTo-Do List Manager.")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_items()

        elif choice == "2":
            create_task()

        elif choice == "3":
            mark_item_complete()

        elif choice == "4":
            print("Goodbye...!")
            break

        else:
            print("Invalid choice.")

main()