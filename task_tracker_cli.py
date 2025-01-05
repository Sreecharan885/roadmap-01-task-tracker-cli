from datetime import datetime
import json

# For adding a task to the file handler object
def add(task_description):
    json_file_object = open('task_database.json','r+')
    data = json.load(json_file_object)
    task = {
        "id": get_latest_id(data) + 1,
        "description": task_description,
        "status": "todo",
        "createdAt": str(get_current_timestamp()),
        "updatedAt": str(get_current_timestamp())
    }
    data["tasks"].append(task)
    json_file_object.seek(0)
    json_file_object.truncate()
    json.dump(data,json_file_object)
    json_file_object.close()

def update(id, task_description):
    json_file_object = open('task_database.json','r+')
    data = json.load(json_file_object)
    updated = False
    for i in data["tasks"]:
        if i["id"] == id:
            i["description"] = task_description
            i["updatedAt"] = str(get_current_timestamp())
            updated = True
    if updated == False:
        print("Task with given id doesn't exist")
    else:
        print("Updated")    
        json_file_object.seek(0)
        json_file_object.truncate()
        json.dump(data,json_file_object)
    json_file_object.close()

def update_status(id, status):
    json_file_object = open('task_database.json','r+')
    data = json.load(json_file_object)
    updated = False
    for i in data["tasks"]:
        if i["id"] == id:
            i["status"] = status
            i["updatedAt"] = str(get_current_timestamp())
            updated = True
    if updated == False:
        print("Task with given id doesn't exist")
    else:
        print("Updated")    
        json_file_object.seek(0)
        json_file_object.truncate()
        json.dump(data,json_file_object)
    json_file_object.close()

def list_tasks(status=None):
    if status not in [None, "todo", "in-progress", "done"]:
        print("Invalid status")
        return
    json_file_object = open('task_database.json','r+')
    data = json.load(json_file_object)
    for i in data["tasks"]:
        if status != None: 
            if i["status"] == status:
                print("Id: ", i["id"])
                print("Description: ", i["description"])
                print("Status: ", i["status"])
                print()
        else:
            print("Id: ", i["id"])
            print("Description: ", i["description"])
            print("Status: ", i["status"])
            print()
    json_file_object.close()

def delete_task(id):
    json_file_object = open('task_database.json','r+')
    data = json.load(json_file_object)
    task_to_delete = ''
    for i in data["tasks"]:
        if i["id"] == id:
            task_to_delete = i
    if task_to_delete == '':
        print("Task doesn't exist")
    else:
        data["tasks"].remove(task_to_delete)
        json_file_object.seek(0)
        json_file_object.truncate()
        json.dump(data,json_file_object)
    json_file_object.close()


# Utility Function
def get_current_timestamp():
    return datetime.now()

# Utility Function
def get_latest_id(data):
    try: 
        return data["tasks"][-1]["id"]
    except Exception as e:
        return 0

# Utility Function 
# Closes any file handler it opens
# Used in commands other than 'add'
def file_exists():
    try:
        with open('task_database.json', 'r') as file: 
            file.close()
            return True
    except FileNotFoundError: 
        return False
    
# Utility function for error messages    
def invalid_command(message):
    print(f"Invalid usage. {message}. Please use 'help' for usage")

# Utility function to split the commands while considering quoted strings as one
def custom_split(command):
    parsed_list = []
    flag = False
    word = ""
    for i in command:
        if i != ' ' and i != '"':
            word += i
        elif i == ' ':
            if flag == False:
                parsed_list.append(word)
                word = ''
            else:
                word += i
        elif i == '"':
            flag = not flag
    if len(word) != 0:
        parsed_list.append(word)
    return parsed_list

def main():
    # Write the core logic for Command line interaction here using match
    break_flag = False
    while not break_flag:
        print()
        command = input('task-cli ')
        parse_command = custom_split(command=command)
        # print(parse_command)
        try:
            main_command = parse_command[0]
        except:
            continue
        command_length = len(parse_command)

        if main_command not in ['add','quit']:
            if not file_exists():
                print("No tasks available. Add a task to continue")
                continue

        match main_command:
            case 'add':
                if command_length != 2:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                task_description = parse_command[1]
                add(task_description=task_description)
            case 'list':
                if command_length < 1 and command_length > 2:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                else:
                    if command_length == 2:
                        list_tasks(status=parse_command[1])
                    else:
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
                delete_task(task_id)
            case 'mark-in-progress' | 'mark-done':
                if command_length != 2:
                    invalid_command("The number of parameters is not correct for the given command")
                    continue
                task_id = int(parse_command[1])
                if main_command == 'mark-in-progress':
                    update_status(task_id,"in-progress")
                elif main_command == 'mark-done':
                    update_status(task_id,"done")
            case 'quit':
                break_flag = True
            case _:
                invalid_command("The command doesn't exist")

if __name__ == "__main__":
    main()