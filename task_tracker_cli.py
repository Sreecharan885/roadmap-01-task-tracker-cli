from utility_functions.file_exist import file_exists
from utility_functions.invalid_command import invalid_command
from utility_functions.custom_split import custom_split

from commands.add_task import add
from commands.update_task import update, update_status
from commands.list_task import list_tasks
from commands.delete_task import delete_task
from commands.help import help

def main():
    # Write the core logic for Command line interaction here using match
    break_flag = False
    while not break_flag:
        print()
        command = input('task-cli ')
        parse_command = custom_split(command=command)
        
        # When nothing is typed
        try:
            main_command = parse_command[0].lower()
        except:
            continue
        command_length = len(parse_command)

        commands = ['add','update','delete','list','mark-done','mark-in-progress','help','quit']

        if main_command not in commands:
            invalid_command("No such command exists")
            continue

        match main_command:
            case 'add':
                if command_length != 2:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                task_description = parse_command[1]
                add(task_description=task_description)

            case 'list':
                if command_length < 1 or command_length > 2:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                else:
                    if command_length == 2:
                        try:
                            status = status=parse_command[1].lower()
                        except:
                            status = "Invalid"
                        if status not in [None, "todo", "in-progress", "done"]:
                            print("Invalid status")
                            continue
                        if not file_exists():
                            print("No tasks available. Add a task to continue")
                            continue
                        list_tasks(status=status)
                    else:
                        if not file_exists():
                            print("No tasks available. Add a task to continue")
                            continue
                        list_tasks()

            case 'update':
                if command_length != 3:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                try:
                    task_id = int(parse_command[1])
                except:
                    print("Invalid task id")
                    continue     
                if not file_exists():
                    print("No tasks available. Add a task to continue")
                    continue           
                task_description = parse_command[2]
                update(task_id,task_description)

            case 'delete':
                if command_length != 2:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                try:
                    task_id = int(parse_command[1])
                except:
                    print("Invalid task id")
                    continue
                if not file_exists():
                    print("No tasks available. Add a task to continue")
                    continue   
                delete_task(task_id)

            case 'mark-in-progress' | 'mark-done':
                if command_length != 2:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                try:
                    task_id = int(parse_command[1])
                except:
                    print("Invalid task id")
                    continue
                if not file_exists():
                    print("No tasks available. Add a task to continue")
                    continue
                if main_command == 'mark-in-progress':
                    update_status(task_id,"in-progress")
                elif main_command == 'mark-done':
                    update_status(task_id,"done")

            case 'help':
                if command_length != 1:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                help()
                
            case 'quit':
                if command_length != 1:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                break_flag = True
                
            case _:
                invalid_command("Invalid usage")

if __name__ == "__main__":
    main()