from datetime import datetime
import json
from pathlib import Path

# Task class that contains properties of each created task
class Task:
    def __init__(self, description, status='todo', tags=None):
        self.description = description  # Description of the task
        self.status = status  # Status of the task, default is 'todo'
        self.createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp when the task was created
        self.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp when the task was last updated
        self.tags = tags if tags else []  # Store tags as a list

# Task-tracker class to handle adding, deleting, updating, and viewing of tasks
class TaskTracker:
    def __init__(self, path):
        self.tasks = {}  # Dictionary to store tasks with their IDs
        self.current_id = 1  # Initialize current ID for tasks
        self.path = path
        self.load_tasks()  # Load tasks from JSON on initialization

    def load_tasks(self):
        # Load tasks from the JSON file if it exists
        if self.path.exists():
            with open(self.path, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = {int(k): v for k, v in tasks_data.items()}  # Convert keys back to int
                self.current_id = max(self.tasks.keys()) + 1 if self.tasks else 1  # Update current_id

    def save_tasks(self):
        # Save current tasks to the JSON file
        with open(self.path, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, description, status='todo', tags=None):
        # Create a new task and add it to the tasks dictionary
        task = Task(description, status, tags)
        self.tasks[self.current_id] = {
            'Task': task.description,
            'Status': status,
            'Created_At': task.createdAt,
            'Updated_At': task.updatedAt,
            'Tags': task.tags
        }
        self.current_id += 1  # Increment the current ID for the next task
        self.save_tasks()  # Save tasks after adding
        return f'{task.description} task added to list'
    
    def delete_task(self, id):
        # Delete a task by its ID if it exists
        if id in self.tasks:
            task_name = self.tasks[id]['Task']  # Store task name for the return message
            del self.tasks[id]  # Remove the task from the dictionary
            self.save_tasks()  # Save tasks after deletion
            return f"'{task_name}' task successfully deleted"
        else:
            return f"Task with task id {id} not found"
    
    def update_task(self, id, updated_description):
        # Update the description of an existing task
        if id in self.tasks:
            old_description = self.tasks[id]['Task']  # Store old description for the return message
            self.tasks[id]['Task'] = updated_description  # Update the task's description
            self.tasks[id]['Updated_At'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_tasks()  # Save tasks after updating
            return f"{old_description} updated to {updated_description}"
        else:
            return f"Task with task id {id} not found"

    def mark_done(self, id):
        # Mark a task as done
        if id in self.tasks:
            self.tasks[id]['Status'] = 'done'  # Change the status to 'done'
            self.save_tasks()  # Save tasks after marking done
            return f"{self.tasks[id]['Task']} is done"
        else:
            return f"Task with task id {id} not found"
    
    def mark_in_progress(self, id):
        # Mark a task as in progress
        if id in self.tasks:
            self.tasks[id]['Status'] = 'in-progress'  # Change the status to 'in-progress'
            self.save_tasks()  # Save tasks after marking in progress
            return f"{self.tasks[id]['Task']} is currently in progress"
        else:
            return f"Task with task id {id} not found"
    
    def list_tasks(self, status = None):
        # List all tasks, optionally filtered by status
        if status:
            filtered_tasks = [details['Task'] for details in self.tasks.values() if details['Status'] == status]
            return filtered_tasks if filtered_tasks else f"No tasks found with status '{status}'"
        return [details['Task'] for details in self.tasks.values()]
    
    def list_done(self):
        # List all tasks that are marked as done
        list_done = [details['Task'] for details in self.tasks.values() if details['Status'] == 'done']
        return list_done if list_done else "Oops, looks like no tasks have been done"

    def list_in_progress(self):
        # List all tasks that are currently in progress
        list_in_progress = [details['Task'] for details in self.tasks.values() if details['Status'] == 'in-progress']
        return list_in_progress if list_in_progress else "No tasks are currently in progress"
    
    def list_todo(self):
        # List all tasks that are either todo or in progress
        list_todo = [details['Task'] for details in self.tasks.values() if details['Status'] in ['todo', 'in-progress']]
        return list_todo if list_todo else "Looks like we are all clear, you don't have any tasks to do"

# Initialize the path for the JSON file
path = Path('tasks.json')

# Initialize an instance of the task_tracker class
task_tracker = TaskTracker(path)