#!/usr/bin/python3
''' Export data to JSON.'''
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    usersResponse = requests.get(f'{url}/users/')
    users = usersResponse.json()
    data_to_export = {}
    for user in users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        payload = {"userId": USER_ID}
        todo_response = requests.get(f'{url}/todos', params=payload)
        todo = todo_response.json()
        for item in todo:
            task_info = {
                "task": item.get('title'),
                "completed": item.get('completed'),
                "username": USERNAME
            }
            # check if USER_ID already exists as a key
            if USER_ID in data_to_export:
                data_to_export[USER_ID].append(task_info)
            else:
                # If USER_ID is not a key, create a new list and append
                # task_info to it
                data_to_export[USER_ID] = [task_info]

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data_to_export, json_file)
