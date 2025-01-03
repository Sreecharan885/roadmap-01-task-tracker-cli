from datetime import datetime

def add(json_file_object, task_description):
    task = {
        "id": get_latest_id(json_file_object) + 1,
        "description": task_description,
        "status": "todo",
        "createdAt": get_current_timestamp(),
        "updatedAt": get_current_timestamp()
    }
    json_file_object.append(task)
    return json_file_object

# Utility Function
def get_latest_id(json_file_object):
    return json_file_object[-1]["id"]

# Utility Function
def get_current_timestamp():
    return datetime.now()

# Utility Function 
# Used in commands other than 'add'
def check_and_return_file():
    try:
        with open('task_database.json', 'r') as file: 
            return (True, file)
    except FileNotFoundError: 
        print("The file does not exist.")
        return (False, None)

# Utility Function
# Create only when handling 'add' command
def create_task_database():
    file_exists = check_and_return_file()

    if file_exists[0]:
        file_exists[1].close()
        return (False, "file already exists")
    
    with open('task_database.json', 'w') as file:
        file.write("[]")
        file.close()
        return (True, "file created")

def main():
    # Write the core logic for Command line interaction here using switch
    pass

if __name__ == "__main__":
    main()