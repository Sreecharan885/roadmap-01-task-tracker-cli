1. Is a CLI application just like a while loop running forever?
   1. Using `while` for now.
   2. `Later` We can check the `cmd` library from Python
2. What information to store about a task in JSON?
   1. Id
      1. Get the latest ID from JSON (UF)
      2. Increment it by 1 and use it.
   2. Description
   3. Status
   4. createdAt
   5. updatedAt
3. In what order to store the information in JSON?
   1. Because there is no requirement to sort, we'll just store them one after another for now.
4. Some useful utility functions (UF)
   1. Get the latest ID from the JSON
   2. Get the current timestamp
   3. Check if the JSON file exists (should be first check)
5. Some tasks get deleted after some time leaving their IDs unused, should we use them?
   1. No, let's use `latest+1`
6. Do we save the file after every update to the tasks? Or do we save it only after the session is closed maintaining the latest info only as an dictionary object until then?
   1. Let's save after every just update so that even if the program crashes midway, all the updates so far are saved
      1. You can flush the file buffer. This way you don't have to close and open the connection after every change.
   2. `Later` We can give an explicit command to commit all the operations performed so far.
7. What commands can we use as positional arguments to add/update the task's configuration?
   1. `add` `description` - To add a new task
   2. `update` `id` `description` - To update an existing task
   3. `delete` `id` - To delete an existing task
   4. `list` - To list all the tasks
      1. `list` `status` - To list all the tasks based on the status
   5. `mark-<status>` `id` - To mark a task based on the given status
   6. `help` - Gives user information about the tasks
   7. `quit` - To stop the application
8. Tasks in detail
   1. `add`
      1. Create a task, assign its status to todo
9.  How do you choose the command?
   1. Use a `switch` statement.
10. General Error scenarios
   1. The JSON file itself doesn't exist and operations other than `add` are used
      1. Inform that no tasks exist after confirming that JSON file doesn't exist.
   2. Using a command that doesn't exist
      1. Inform that it's not a valid command, and ask the user to utilize `help` for more information
   3. Using a command that exists but number of parameters is less than what's expected of that command
      1. Inform that the usage is not correct, and ask the user to utilize `help` for more information
   4. Using a command that exists but number of parameters is more than what's expected of that command
      1. If the data types are correct, ask if the user wants to proceed further with some loss of data, if yes, go ahead.
   5. Using a command that exist and also using correct number of arguments for that command but the request fails for some reason - Specific to each command. Refer to the next point.
11. Error scenarios for commands in specific
   1.  `add`
       1. `Later` If the user gives a descripition that already matches an existing task. Inform the user that a task with the existing name already exists, and find out if they really want to proceed. If yes, create it anyway. -> This search would cause a delay when string matching.
   2.  `update`
       1.  If the id doesn't exist, inform that the id doesn't exist
       2.  If the parameter order is reversed, inform that the command expects the parameters in a proper order.
   3.  `delete`
       1.  If the id doesn't exist, inform that the id doesn't exist
12. Regarding `help`
    1.  For each command
        1.  Specify the exact usage with an example