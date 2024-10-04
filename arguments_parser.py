import argparse
# Create the parser
parser = argparse.ArgumentParser(description="Task CLI")

# Create Subparsers for different commands
subparsers = parser.add_subparsers(dest='command')

# Add task
add_parser = subparsers.add_parser('add', help='Add a new task')
add_parser.add_argument('task', type=str, help='Task description')
add_parser.add_argument('--tags', nargs='*', help='List of tags for the task')

# Update task
update_parser = subparsers.add_parser('update', help='Update an existing task')
update_parser.add_argument('task_id', type=int, help='Task ID')
update_parser.add_argument('new_task', type=str, help="New task description")

# Delete task
delete_parser = subparsers.add_parser('delete', help='Delete a task')
delete_parser.add_argument('task_id', type=int, help='Task ID')

# Mark task as in progress
mark_in_progress_parser = subparsers.add_parser('mark_in_progress', help='Mark a task as in progress')
mark_in_progress_parser.add_argument('task_id', type=int, help='Task ID')

# Mark task as done
mark_done_parser = subparsers.add_parser('mark_done', help="Mark a task as done")
mark_done_parser.add_argument("task_id", type=int, help="Task ID")

# List tasks
list_parser = subparsers.add_parser('list', help='List tasks')
list_parser.add_argument('status', nargs="?", choices=['todo', 'in-progress', 'done'], help='Filter by status')

# Parse the arguments
args = parser.parse_args()