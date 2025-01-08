import json

def list_tasks(status=None):
    json_file_object = open('task_database.json','r+')
    data = json.load(json_file_object)
    count = 0
    for i in data["tasks"]:
        if status != None: 
            if i["status"] == status:
                print("Id: ", i["id"])
                print("Description: ", i["description"])
                print("Status: ", i["status"])
                print()
                count += 1
        else:
            print("Id: ", i["id"])
            print("Description: ", i["description"])
            print("Status: ", i["status"])
            print()
            count += 1
    if count == 0:
        if status != None:
            print("No tasks available with the specified criteria")
        else:
            print("No tasks available. Add a task to continue")
    json_file_object.close()