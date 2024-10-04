import Task_tracker as task_tracker
import arguments_parser as args



def main():
    if args.args.command == 'add':
        tags = args.args.tags if args.args.tags else []
        print(task_tracker.task_tracker.add_task(args.args.task, tags=tags))
    elif args.args.command == 'update':
        print(task_tracker.task_tracker.update_task(args.args.task_id, args.args.new_task))
    elif args.args.command == 'delete':
        print(task_tracker.task_tracker.delete_task(args.args.task_id))
    elif args.args.command == 'mark_in_progress':
        print(task_tracker.task_tracker.mark_in_progress(args.args.task_id))
    elif args.args.command == 'mark_done':
        print(task_tracker.task_tracker.mark_done(args.args.task_id))
    elif args.args.command == 'list':
        if args.args.status == 'todo':
            print(task_tracker.task_tracker.list_todo())
        elif args.args.status == 'done':
            print(task_tracker.task_tracker.list_done())
        elif args.args.status == 'in-progress':
            print(task_tracker.task_tracker.list_in_progress())
        else:
            print("Invalid status. Please use 'todo', 'done', or 'in-progress'.")

if __name__ == '__main__':
    main()