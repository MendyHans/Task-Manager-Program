# ===== Importing libraries ========
import os
from datetime import datetime

# ==== Function Definitions ====

# Load users from the user.txt file into a dictionary
def load_users(file_path="user.txt"):
    """
    Reads the user.txt file and stores usernames and passwords in a dictionary.
    Returns the dictionary of users.
    """
    users = {}
    if os.path.exists(file_path):  # Check if the file exists
        with open(file_path, "r") as f:
            for line in f:
                username, password = line.strip().split(", ")
                users[username] = password
    return users

# Save a new user to the user.txt file
def save_user(username, password, file_path="user.txt"):
    """
    Appends a new username and password to the user.txt file.
    """
    with open(file_path, "a") as f:
        f.write(f"{username}, {password}\n")

# Login function to validate user credentials
def login(users):
    """
    Prompts the user to enter their username and password.
    Validates the input against the users dictionary.
    Returns the username of the logged-in user.
    """
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            return username  # Return the logged-in user's username
        print("Invalid username or password. Please try again.")

# Register a new user
def register_user(users):
    """
    Allows the admin to register a new user.
    Verifies that passwords match and adds the user to the user.txt file.
    """
    new_username = input("Enter a new username: ")
    if new_username in users:
        print("Username already exists. Try again.")
        return
    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm your password: ")
    if new_password == confirm_password:
        save_user(new_username, new_password)
        print("User registered successfully!")
    else:
        print("Passwords do not match. Try again.")

# Add a new task to the task.txt file
def add_task(file_path="task.txt"):
    """
    Prompts the user for task details, including assigned user, title, description, 
    due date, and current date. Saves the task to the task.txt file.
    """
    assigned_user = input("Enter the username of the person assigned to the task: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date
    task_data = f"{assigned_user}, {title}, {description}, {due_date}, {current_date}, No\n"
    with open(file_path, "a") as f:
        f.write(task_data)
    print("Task added successfully!")

# View all tasks in the task.txt file
def view_all_tasks(file_path="task.txt"):
    """
    Reads all tasks from the task.txt file and displays them in a user-friendly format.
    """
    if os.path.exists(file_path):  # Check if the file exists
        with open(file_path, "r") as f:
            for line in f:
                assigned_user, title, description, due_date, current_date, status = line.strip().split(", ")
                print(f"""
Task:            {title}
Assigned to:     {assigned_user}
Date assigned:   {current_date}
Due date:        {due_date}
Task complete?   {status}
Task description:
  {description}
                """)
    else:
        print("No tasks found.")

# View tasks assigned to the logged-in user
def view_my_tasks(username, file_path="task.txt"):
    """
    Reads tasks from the task.txt file and displays only the tasks assigned to the logged-in user.
    """
    if os.path.exists(file_path):  # Check if the file exists
        with open(file_path, "r") as f:
            tasks_found = False  # Flag to check if tasks exist for the user
            for line in f:
                assigned_user, title, description, due_date, current_date, status = line.strip().split(", ")
                if assigned_user == username:
                    tasks_found = True
                    print(f"""
Task:            {title}
Assigned to:     {assigned_user}
Date assigned:   {current_date}
Due date:        {due_date}
Task complete?   {status}
Task description:
  {description}
                    """)
            if not tasks_found:
                print("No tasks assigned to you.")
    else:
        print("No tasks found.")

# Main function
def main():
    """
    Main function to run the task management system.
    Loads user credentials, handles login, and provides menu options.
    """
    # Load users from file
    users = load_users()

    # Login the user
    current_user = login(users)

    # Menu options
    while True:
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

        if menu == 'r' and current_user == "admin":  # Only admin can register users
            register_user(users)
            users = load_users()  # Reload users to update the dictionary
        elif menu == 'r':
            print("Only the admin can register new users.")
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks(current_user)
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have entered an invalid input. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
