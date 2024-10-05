# Task Tracker CLI APP

This is a CLI app used to track and manage your tasks. It allows you to track what you need to do, what you have done, and what you are currently working on. This CLI app was built using only Python's native file system module.

## How to use this project
The list of commands and their usage is given below:

# Adding a new task
python3 task-cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
python3 task-cli.py update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
python3 task-cli.py mark-in-progress 1
python3 task-cli.py mark-done 1

# Listing all tasks
python3 task-cli.py list

# Listing tasks by status
python3 task-cli.py list done
python3 task-cli.py list todo
python3 task-cli.py list in-progress


# Project Link
https://roadmap.sh/projects/task-tracker
