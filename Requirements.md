- `Objective` To track and manage your tasks

- `Overview`
	- CLI 
	- Track
		- What you need to do
		- What you have done
		- What you're currently working on

- `Areas of improvement`
	- Programming skills
	- Working with the file system
	- Handling user inputs
	- Building simple CLI application

- `Requirements`
	- Application should run from command line
	- Accept user actions and inputs as arguments
	- Store the tasks in a JSON file
	- User should be able to
		- Add, Update, and Delete tasks
		- Mark a task as in progress or done
		- List all tasks
		- List all tasks that are
			- done
			- not done
			- in progress
	
	- Constraints
		- Any programming language can be used
		- Positional arguments in CMD to accept user inputs
		- Use a JSON file to store the tasks in the current directory
		- The JSON file should be created if it does not exist
		- Use the **native file system module** of your programming language to interact with the JSON file
		- **Do not use any external libraries or frameworks to build this project**
		- Ensure to handle errors and edge cases gracefully


	- Properties of a task
		1. id - a unique id for the task
		2. description - a short description of the task
		3. status - status of the task (todo/ in-progress/ done)
		4. createdAt - The date and time when the task was created
		5. updatedAt - The date and time when the task was last updated

		- Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.

	