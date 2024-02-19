#!/usr/bin/python3
''' Returns information about TODO list progress of an employee.'''
import requests
from sys import argv

if __name__ == "__main__":
    emId = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    usersResponse = requests.get(f'{url}/users/{emId}')
    user = usersResponse.json()
    name = user['name']

    payload = {"userId": emId}
    todo_response = requests.get(f'{url}/todos', params=payload)
    todo = todo_response.json()
    totalTasks = 0
    doneTasks = 0
    taskTitles = []
    for item in todo:
        totalTasks += 1
        if item['completed']:
            doneTasks += 1
            taskTitles.append(item['title'])
    print(f'Employee {name} is done with tasks({doneTasks}/{totalTasks}):')
    for title in taskTitles:
        print(f'\t {title}')
    # print(todo)
