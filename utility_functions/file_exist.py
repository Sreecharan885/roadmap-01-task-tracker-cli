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