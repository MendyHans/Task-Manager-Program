# Task Management System

## Overview
This is a simple command-line task management system that allows users to register, log in, and manage tasks. The system supports adding tasks, viewing all tasks, and viewing tasks assigned to the logged-in user.

## Features
- **User Authentication**: Users must log in to access the system.
- **Admin Registration**: Only the admin can register new users.
- **Task Management**: Users can add tasks and view tasks assigned to them.
- **Task Storage**: Tasks and users are stored in text files (`user.txt` and `task.txt`).

## Installation
1. Ensure you have Python installed on your system.
2. Download or clone the repository.
3. Run the script using:
   ```sh
   python task_manager.py
   ```

## Usage
### 1. User Login
Upon running the script, users are prompted to enter their credentials. Credentials are stored in `user.txt`.

### 2. Menu Options
Once logged in, users can choose from the following options:
- `r` - Register a new user (Admin only)
- `a` - Add a new task
- `va` - View all tasks
- `vm` - View tasks assigned to the logged-in user
- `e` - Exit the program

### 3. Registering Users
- Only the admin can register new users.
- The admin must enter a unique username and matching password confirmation.

### 4. Adding Tasks
- Users can assign tasks to themselves or other users.
- Tasks require a title, description, due date, and are stored in `task.txt`.

### 5. Viewing Tasks
- **View All Tasks (`va`)**: Displays all tasks.
- **View My Tasks (`vm`)**: Displays tasks assigned to the logged-in user.

## File Structure
- `user.txt`: Stores usernames and passwords in `username, password` format.
- `task.txt`: Stores tasks in `assigned_user, title, description, due_date, current_date, status` format.

## License
This project is open-source and free to use.

## Author
Developed by [Mendy]

