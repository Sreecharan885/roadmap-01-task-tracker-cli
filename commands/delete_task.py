import json

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
        print("Task deleted succesfully")
    json_file_object.close()