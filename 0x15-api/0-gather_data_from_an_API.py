#!/usr/bin/python3
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
    print(todo)
