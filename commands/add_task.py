from utility_functions.get_current_timestamp import get_current_timestamp
from utility_functions.get_latest_id import get_latest_id
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