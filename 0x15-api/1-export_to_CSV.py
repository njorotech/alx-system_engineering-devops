#!/usr/bin/python3
''' Export data in the CSV format.'''
import csv
import requests
from sys import argv

if __name__ == "__main__":
    emId = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    usersResponse = requests.get(f'{url}/users/{emId}')
    user = usersResponse.json()
    name = user['name']
    filename = f'{emId}.csv'

    payload = {"userId": emId}
    todo_response = requests.get(f'{url}/todos', params=payload)
    todo = todo_response.json()

    with open(filename, mode='w') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                quotechar='"', quoting=csv.QUOTE_ALL)

        # writer.writeheader()

        for item in todo:
            if item['completed']:
                status = 'True'
            else:
                status = 'False'
            writer.writerow({'USER_ID': f'{emId}', 'USERNAME': f'{name}',
                             'TASK_COMPLETED_STATUS': f'{status}',
                             'TASK_TITLE': f'{item["title"]}'})
