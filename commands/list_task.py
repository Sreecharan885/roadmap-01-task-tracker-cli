import json

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