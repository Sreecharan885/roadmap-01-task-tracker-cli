def help():
    print()
    print("Commands: ")
    print("task-cli add [task-description]              - to add a task with a description (in quotes)")
    print("task-cli update [id] [task-description]      - to update the description (in quotes) of a task with a given id")
    print("task-cli list                                - to list the available tasks")
    print("task-cli delete [id]                         - to delete the task with given id")
    print("task-cli mark-in-progress [id]               - to update the status of the task with given id to 'in-progress'")
    print("task-cli mark-done [id]                      - to update the status of the task with given id to 'done'")
    print("task-cli quit                                - to quit the CLI application")
    print("task-cli help                                - to get help related to the commands")
    