#!/usr/bin/python3
''' Export data to JSON.'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    emId = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    usersResponse = requests.get(f'{url}/users/{emId}')
    user = usersResponse.json()
    username = user['username']
    filename = f'{emId}.json'

    payload = {"userId": emId}
    todo_response = requests.get(f'{url}/todos', params=payload)
    todo = todo_response.json()
    # print(todo)
    data_to_export = {emId: []}
    # print(data_to_export)
    for item in todo:
        task_info = {
            "task": item.get('title'),
            "completed": item.get('completed'),
            "username": username
        }
        data_to_export[emId].append(task_info)
    with open(filename, 'a') as json_file:
        json.dump(data_to_export, json_file)
