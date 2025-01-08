Hey,

This is [the first project from the Backend roadmap in Roadmap.sh](https://roadmap.sh/projects/task-tracker). It is a CLI application that can be used for tracking tasks.

## Doc:
1. `add` `description` - To add a new task with the given description
2. `update` `id` `description` - To update an existing task with the given id to the given description
3. `delete` `id` - To delete an existing task with the given id
4. `list` - To list all the tasks
5. `list` `status` - To list all the tasks based on the status
6. `mark-<status>` `id` - To mark a task's status to the given status (to-do, in-progress)
7. `help` - To understand how to use all the commands in this app
8. `quit` - To stop the application

## Usage
1. Clone the repository to your local system using the following commands
   - `git clone https://github.com/Sreecharan885/roadmap-01-task-tracker-cli.git`
2. Navigate into the project directory
   - `cd roadmap-01-task-tracker-cli`
3. Run the task_tracker_cli.py
   - `python task_tracker_cli.py` / `py task_tracker_cli.py`