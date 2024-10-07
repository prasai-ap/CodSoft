import os

def create_todo_list():
    todolist = []
    n = int(input("Enter the number of tasks to be performed within the day: "))
    
    with open('todolist.txt', 'w') as file:
        for i in range(n):
            task = input(f"Enter task {i + 1}: ")
            todolist.append(task)
            file.write(task + '\n')
    print("Tasks have been created and saved.")

def update_todo_list():
    n = int(input("Enter the number of tasks to be added: "))
    
    with open('todolist.txt', 'a') as file:
        for i in range(n):
            task = input(f"Enter new task {i + 1}: ")
            file.write(task + '\n')
    print("Tasks have been updated.")

def delete_todo_list():
    if os.path.exists("todolist.txt"):
        os.remove("todolist.txt")
        print("To-do list deleted successfully.")
    else:
        print("To-do list does not exist or is already deleted.")

def view_todo_list():
    if os.path.exists("todolist.txt"):
        with open('todolist.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Your To-Do List:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("Your To-Do List is empty.")
    else:
        print("To-Do list file not found.")

def main():
    print("Choose an option:")
    print("1: Create")
    print("2: Update")
    print("3: Delete")
    print("4: View/Track")
    
    option = int(input("Enter your choice: "))
    
    if option == 1:
        create_todo_list()
    elif option == 2:
        update_todo_list()
    elif option == 3:
        delete_todo_list()
    elif option == 4:
        view_todo_list()
    else:
        print("Invalid option! Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
