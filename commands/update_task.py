from utility_functions.get_current_timestamp import get_current_timestamp
import json

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
        json_file_object.seek(0)
        json_file_object.truncate()
        json.dump(data,json_file_object)
        print("Updated task's description successfully")
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
        print("Updated tasks's status successfully")    
        json_file_object.seek(0)
        json_file_object.truncate()
        json.dump(data,json_file_object)
    json_file_object.close()